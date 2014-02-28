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
		self.nodes = [BayesianNode(self.network) for i in range(1,10)]

	def test_baseFunctionality(self):
		for i in range(len(self.nodes)):
			self.nodes[i].addParent(self.nodes[i])
		
		for node in self.nodes:
			self.assertEqual(node.network, self.network)

	def test_parenting(self):
		# Test parenting
		for i in range(2, len(self.nodes)):
			self.nodes[i].addParent(self.nodes[i-1])

	def test_positions(self):
		# Test position assignment
		for node in self.nodes:
			self.assertEqual(node.position[0], 25)
			self.assertEqual(node.position[1], 25)

	def test_quadTreeInsertAndRetrieve(self):
		self.lol = 3

	def test_nodeParents(self):
		self.lol = 3

	def test_connections(self):
		self.lol = 3

	def test_mapManagerSelectsCorrectNodes(self):
		self.lol = 3