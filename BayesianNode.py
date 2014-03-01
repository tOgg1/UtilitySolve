from PyGameHelpers import *
from Misc import errorPrint as er, debugPrint as db, normalPrint as pr
from Misc import *

class BayesianNode:

	image = None
	imageRect = None
	imageHighlighted = None
	imageHighlightedRect = None
	imageConnection = None
	imageConnectionRect = None

	@staticmethod
	def loadImages(setSize = None):
		BayesianNode.image, BayesianNode.imageRect = loadImage("circle.png")
		BayesianNode.imageHighlighted, BayesianNode.imageHighlightedRect = loadImage("circle_highlighted.png")
		#BayesianNode.imageConnection, BayesianNode.imageConnectionRect = loadImage("arrow.png")		

	def __init__(self, network = None):
		self.network = network
		self.parents = []
		self.connections = []
		self.values = []
		self.CPT = []
		self.finalized = False
		self.position = [0, 0]
		self.size = 0
		self.observable = True
		self.name = "DefaultNode"
		self.currentValue = None
		
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setNetwork(self, network):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform setNetwork.")
			return
		self.network = network

	def addValue(self, value):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform addValue.")
			return
		# Set first value added as default value
		if(self.currentValue == None):
			self.currentValue = value
		self.values.append(value)

	def getValues(self):
		return self.values

	def getCurrentValue(self):
		return self.currentValue

	def setCurrentValue(self, value):
		if not value in self.values:
			er("Value does not exist in node")
			return
		self.currentValue = value

		# Update CPT's, if finalized
		if self.finalized:
			relevantRow = self.values.index(value)

			for row in self.CPT:
				for valuePair in row:
					valuePair[1] = 0

			for valuePair in self.CPT[relevantRow]:
				valuePair[1] = 1

	def addParent(self, parent):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform addParent.")
			return

		self.parents.append(parent)

		connection = Connection(self, parent)
		self.addConnection(connection)
		parent.addConnection(connection)

	def addParents(self, parents):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform addParents.")
			return
		for parent in self.parents:
			self.addParent(parent)

	def removeParent(self, parent):
		if parent in self.parents:
			self.parents.remove(parent)

		self.removeConnectionTo(parent)

	def getParents(self):
		return self.parents

	def finalize(self):
		if(self.finalized == True):
			er("[Node]: Node is already finalized. Please call definalize if you want to refinalize.")

		if(self.network == None):
			er("[Node]: Can't finalize a node which is not a part of a network, please call \"setNetwork()\"")

		self.finalized = True

		if(len(self.parents) == 0):
			if not self.observable:
				self.CPT = [[0] for i in range(len(self.values))]
				for i in range(0,len(self.values)):
					pr("[Node]: Please specify probability for " + self.getName() + " = " + str(self.values[i]))
					ans = parseInputToNumber(input("Answer: "))
					self.CPT[i] = ([[None, None]], ans)
					return
			else:
				self.CPT = [[0] for i in range(len(self.values))]
				for i in range(len(self.values)):
					self.CPT[i] = ([[None, None]], 1/len(self.values))	
					return

		# Create CPT's
		valueLists = [[parent, parent.getValues()] for parent in self.parents]

		totalLength = 1
		for parent, valueSet in valueLists:
			totalLength *= len(valueSet)

		pr("[Node]: Finalizing node with a CPT of total size " + str(totalLength*len(self.values)))

		self.CPT = [[0]*totalLength for i in range(len(self.values))]

		if(self.observable == True):
			pr("[Node]: This node is observable. You should therefore make sure only one variable per row/column is set.\n[Node]: The CPT will be normalized automatically.")
		else:
			pr("[Node]: This node is not observable. All column/row-combinations can contain information.\n[Node]: The CPT will be normalized automatically")
		emptyArray = []

		i = 0
		for value in self.values:
			self.getListPossibleValues(self.CPT, i, 0, [self, value], emptyArray, list(valueLists))
			i = i+1

	def getListPossibleValues(self, cpt, i, j, rootTuple, currentSetValues, remainingList):
		# If we're at the bottom of the chain
		if len(remainingList) == 0:
			pr("[Node]: Please specify probability of " + str(rootTuple[0].getName()).upper() + " = " + str(rootTuple[1]).upper() + " given: ")
			for parent, value in currentSetValues:
				pr(str(parent.getName()) + " = " + value)
			ans = parseInputToNumber(input("Answer: "))
			cpt[i][j] = (list(currentSetValues), ans)
			return

		# Else 
		valueTuple = remainingList.pop()
		parent = valueTuple[0]
		values = valueTuple[1]

		for value in values:
			currentSetValues.append([parent, value])
			self.getListPossibleValues(cpt, i, j, rootTuple, currentSetValues, list(remainingList))
			currentSetValues.remove([parent, value])
			j = j+1

	def definalize(self):
		self.finalized = False

	def setObservable(self, boolean):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform setObservable.")
			return
		for parent in self.parents:
			if not parent.observable:
				er("[Node]: Cannot make node observable if parent is unobservable "+
				   "(this does not make any logical sense)")
				return
		self.observable = boolean

	def getProbabilityOfValue(self, value):
		if not value in self.values:
			er("[Node]: Value is not in self.values")
		
		# Find row
		row = self.values.index(value)

		# Set start, we assume a start prob of 0
		probability = 0
		

		# If this is observable we can really just check if the value passed in
		# is the same as the currently set value
		if(self.observable):
			if(value == self.currentValue):
				return 1
			else:
				return 0
		else:
			for valueTuple in self.CPT[row]:
				nodeProb = valueTuple[1]

				for parent, value in valueTuple[0]:
					if not parent == None:
						nodeProb *= parent.getProbabilityOfValue(value)	

				probability += nodeProb
		return probability

	def getProbabilityOfTuple(self, value):
		if(isinstance(parent, str)):
			for row in self.CPT:
				for valuePair in row:
					if(valuePair[0][0].getName() == parent and valuePair[0][1] == value):
						return valuePair[1]

		elif(isinstance(parent, BayesianNode)):
			for row in self.CPT:
				for valuePair in row:
					if(valuePair[0][0] == parent and valuePair[0][1] == value):
						return valuePair[1]

	def setPosition(self, position):
		self.position = position

	def getPosition(self):
		return self.position

	def setSize(self, size):
		self.size = size

	def getRect(self):
		return pygame.Rect(position[0] - size, position[1] - size, size, size)

	def addConnection(self, connection):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform addConnection.")
			return
		self.connections.append(connection)

	def removeConnection(self, connection):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform removeConnection.")
			return
		self.connect
		if connection in self.connections:
			if(connection.getParent() != self):
				connection.getParent().removeConnection(connection)
			self.connections.remove(connection)

	def removeConnectionTo(self, parent):
		if(finalized):
			er("[Node]: Node is already finalized. Can not perform removeConnectionTo.")
			return
		self.connect
		for connection in self.connections:
			if parent == connection.getParent():
				self.connections.remove(connection)
			parent.removeConnection(connection)

	def getConnections(self):
		return self.connections

class Connection:

	def __init__(self, child, parent):
		self.child = child
		self.parent = parent

		#Generate end-points and boundingBox
		self.endPoints = [self.parent.getPosition(), self.child.getPosition()]
		self.size = [abs(self.endPoints[0][0] - self.endPoints[0][1]),
					 abs(self.endPoints[1][0] - self.endPoints[1][1])]

		minX = min(self.parent.position[0], self.child.position[0])
		minY = min(self.parent.position[1], self.child.position[1])

		self.rect = pygame.Rect(minX, minY, self.size[0], self.size[1])

	def getRect(self):
		return self.rect

	def getParent(self):
		return self.parent

	def getChild(self):
		return self.child

	def getNodes(self):
		return [self.parent, self.child]



