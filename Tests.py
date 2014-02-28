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
		# Setup
		for node in self.nodes:
			node.setPosition([25, 25])

		for i in range(len(self.nodes)):
			self.nodes[i].addParent(self.nodes[i])
		
		for node in self.nodes:
			self.assertEqual(node.network, self.network)


		# Test position assignment
		for node in self.nodes:
			self.assertEqual(node.position[0], 25)
			self.assertEqual(node.position[1], 25)

		# Test parenting
		for i in range(len(self.nodes)):

	def test_quadTreeInsertAndRetrieve(self):
		self.lol = 3

	def test_nodeParents(self):
		self.lol = 3

	def test_connections(self):
		self.lol = 3

	def test_mapManagerSelectsCorrectNodes(self):
		self.lol = 3