from PyGameHelpers import *
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
		self.parents = []
		self.connections = []
		self.network = network
		self.values = []
		self.CPT = {}
		self.finalized = False
		self.position = [0, 0]
		self.size = 0
		
	def setNetwork(network):
		self.network = network

	def addValue(self, value):
		values.append(value)

	def addParent(self, parent):
		self.parents.append(parent)

		connection = Connection(self, parent)
		self.addConnection(connection)
		parent.addConnection(connection)

	def addParents(self, parents):
		for parent in self.parents:
			self.addParent(parent)

	def getParents(self):
		return self.parents

	def finalize(self):
		if(self.network == None):
			er("Can't finalize a node which is not a part of a network, please call \"setNetwork()\"")

		self.finalized = True

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

	def getConnections(self):
		return self.connections

class Connection:

	def __init__(self, parent, child):
		self.parent = parent
		self.child = child

		#Generate end-points and boundingBox
		self.endPoints = [self.parent.getPosition(), self.child.getPosition()]
		self.size = [abs(self.endPoints[0][0] - self.endPoints[0][1]),
					 abs(self.endPoints[1][0] - self.endPoints[1][1])]

		minX = min(self.parent.position[0], self.child.position[0])
		minY = min(self.parent.position[1], self.child.position[1])

		self.rect = pygame.Rect(minX, minY, self.size[0], self.size[1])

	def getRect():
		return self.rect

	def getParent():
		return self.parent

	def getChild():
		return self.child

	def getNodes():
		return [self.parent, self.child]



