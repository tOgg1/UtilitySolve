from ProblemBuilder import *
from BayesianNetwork import *
from BayesianNode import *
from MapManager import *

# Class for testing
class TestClass(unittest.TestCase):

	def setUp(self):
		# Init core-objects
		self.mapManager = MapManager([200, 200])
		self.network = BayesianNetwork(self.mapManager)
		self.nodes = [BayesianNode(self.network) for i in range(0,10)]

	def test_baseFunctionality(self):
		for i in range(len(self.nodes)):
			self.nodes[i].addParent(self.nodes[i])
		
		for node in self.nodes:
			self.assertEqual(node.network, self.network)

	def test_nodeParenting(self):
		self.assertEqual(len(self.nodes), 10)

		for i in range(2, len(self.nodes)):
			self.nodes[i].addParent(self.nodes[i-1])

		for node in self.nodes:
			self.assertNotEqual(len(node.getParents()), 0)

		for j in range(len(self.nodes)-1, 1):
			self.assertIn(self.nodes[j], self.nodes[j-1].getParents())

			for i in range(len(self.nodes)):
				if(i != j):
					self.assertIn(self.nodes[i], self.nodes[j-1].getParents())		

	def test_nodePositions(self):
		for node in self.nodes:
			node.setPosition([23, 25])

		# Test position assignment
		for node in self.nodes:
			self.assertEqual(node.position[0], 23)
			self.assertEqual(node.position[1], 25)


	def test_nodeConnections(self):
		self.lol = 3

	def test_nodeValues(self):
		self.lol = 4

	def test_nodeSizes(self):
		self.lol = 4

	def test_quadTreeInsertAndRetrieve(self):
		self.lol = 3

	def test_mapManagerSelectsCorrectNodes(self):
		self.lol = 3