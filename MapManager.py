from QTree import QTree

import pygame

class MapManager:

	mapSize = 32768

	def __init__(self, screenSize, network = None):
		self.position = 0
		self.screenSize = screenSize
		self.network = network
		self.tree = QTree(pygame.Rect(-MapManager.mapSize/2, -MapManager.mapSize/2, 
									   MapManager.mapSize, MapManager.mapSize))

	def addNode(self, node):
		self.tree.insert(node)

	def setNetwork(self, network):
		self.network = network

	def setPosition(self, position):
		self.position = position

	def incrementPosition(self, delta):
		self.position[0] += delta[0]
		self.position[1] += delta[1]

	def getPosition(self, position):
		return self.position

	def getAllNodes(self):
		return self.tree.getAllNodes()

	def getNodesAndConnectionsOnScreen(self):
		relevantNodes = []
		screenRect = pyGame.Rect(self.position[0] 	 - 	self.screenSize[0],
								 self.position[1] 	 - 	self.screenSize[1],
								 self.screenSize[0], 	self.screenSize[1]); 
		relevantNodes.extend(self.tree.getChildrenInRegion(screeRect))

		for node in relevantNodes:
			for connection in node.getConnections():
				if not connection in relevantNodes:
					relevantNodes.append(connection)

		return relevantNodes