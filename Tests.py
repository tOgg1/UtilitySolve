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
		length = len(self.nodes)

		self.nodes[0].addParent(self.nodes[length-1])

		self.assertNotEqual(len(self.nodes[0].getParents()), 0)
		self.assertIn(self.nodes[length-1], self.nodes[0].getParents())

		self.nodes[0].addParent(self.nodes[length-2])
		self.nodes[1].addParent(self.nodes[0])
		self.nodes[1].addParent(self.nodes[length-1])

		self.assertIn(self.nodes[1].getParents()[1], self.nodes[0].getParents())

		self.assertEqual(len(self.nodes[1].getParents()), len(self.nodes[0].getParents()))

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