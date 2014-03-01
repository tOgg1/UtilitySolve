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
		
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setNetwork(self, network):
		self.network = network

	def addValue(self, value):
		self.values.append(value)

	def getValues(self):
		return self.values

	def addParent(self, parent):
		self.parents.append(parent)

		connection = Connection(self, parent)
		self.addConnection(connection)
		parent.addConnection(connection)

	def addParents(self, parents):
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
			er("Node is already finalized. Please call definalize if you want to refinalize.")

		if(self.network == None):
			er("Can't finalize a node which is not a part of a network, please call \"setNetwork()\"")

		self.finalized = True

		# Create CPT's
		valueLists = [[parent, parent.getValues()] for parent in self.parents]

		totalLength = 1
		for parent, valueSet in valueLists:
			totalLength *= len(valueSet)

		pr("Finalizing node with a CPT of total size " + str(totalLength*len(self.values)))

		self.CPT = [[0]*totalLength for i in range(len(self.values))]

		if(self.observable == True):
			pr("This node is observable. You should therefore make sure only one variable per row/column is set.\nIt will be normalized automatically.")
		

		emptyArray = []
		
		i = 0
		for value in self.values:
			emptyArray.append([self, value])
			self.getListPossibleValues(self.CPT, i, 0, [self, value], emptyArray, list(valueLists))
			emptyArray.remove([self, value])
			i = i+1

		print self.CPT


	def getListPossibleValues(self, cpt, i, j, rootTuple, currentSetValues, remainingList):
		# If we're at the bottom of the chain
		if len(remainingList) == 0:
			pr("Please specify probability of " + str(rootTuple[0].getName()).upper() + " equals " + str(rootTuple[1]).upper() + " given: ")
			for parent, value in currentSetValues:
				if not parent == rootTuple[0]:
					pr(str(parent.getName()) + " = " + value)
			ans = parseInputToNumber(input("Answer: "))
			cpt[i][j] = ans
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
		for parent in self.parents:
			if not parent.observable:
				er("Cannot make node observable if parent is unobservable "+
				   "(this does not make sense logically)")
				return
		self.observable = boolean

	def getProbability(self, parent, value):
		self.lol = true

	def setPosition(self, position):
		self.position = position

	def getPosition(self):
		return self.position

	def setSize(self, size):
		self.size = size

	def getRect(self):
		return pygame.Rect(position[0] - size, position[1] - size, size, size)

	def addConnection(self, connection):
		self.connections.append(connection)

	def removeConnection(self, connection):
		if connection in self.connections:
			if(connection.getParent() != self):
				connection.getParent().removeConnection(connection)
			self.connections.remove(connection)

	def removeConnectionTo(self, parent):
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



