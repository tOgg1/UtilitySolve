from ProblemBuilder import *
from BayesianNetwork import *
from BayesianNode import *
from UtilityNode import *
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
		length = len(self.nodes)
		
		self.nodes[0].addParent(self.nodes[length-1])

		# Check if node 0 has a parent
		self.assertNotEqual(len(self.nodes[0].getParents()), 0)
		# Check if the parent is the correct one
		self.assertIn(self.nodes[length-1], self.nodes[0].getParents())

		self.nodes[0].addParent(self.nodes[length-2])
		self.nodes[1].addParent(self.nodes[0])
		self.nodes[1].addParent(self.nodes[length-1])

		# Check if the node added as parent for node 1 is also a parent of node 0
		self.assertIn(self.nodes[1].getParents()[1], self.nodes[0].getParents())
		# Check if the node parent-lenghts are the same, i.e. all parents have been properly added
		self.assertEqual(len(self.nodes[1].getParents()), len(self.nodes[0].getParents()))

	def test_nodePositions(self):
		for node in self.nodes:
			node.setPosition([23, 25])

		# Test position assignment
		for node in self.nodes:
			self.assertEqual(node.position[0], 23)
			self.assertEqual(node.position[1], 25)

		node1, node2 = self.nodes[0], self.nodes[1]

		# Test setPosition and getPosition functions
		node1.setPosition((0,3))
		node2.setPosition((0,4))

		self.assertEqual(node1.position[0], 0)
		self.assertEqual(node1.position[1], 3)

		pos = node1.getPosition()

		self.assertEqual(node1.position, pos)

	def test_nodeConnections(self):
		node1, node2, node3 = self.nodes[0], self.nodes[1], self.nodes[2]

		node1.addParent(node3)
		node2.addParent(node3)
		node1.addParent(node2)

		# Check inheritance
		connections1 = node1.getConnections()
		connections2 = node2.getConnections()
		connections3 = node3.getConnections()

		# Check basic containment
		self.assertNotEqual(len(connections1), 0)
		self.assertNotEqual(connections1, connections2)

		# Check if node1 is the child-part of the first connection in connections1
		self.assertEqual(connections1[0].getChild(), node1)

		parents1 = [connection.getParent() for connection in connections1]
		parents2 = [connection.getParent() for connection in connections2]

		self.assertIn(node2, parents1)
		self.assertIn(node3, parents1)

		for parent in parents2:
			self.assertIn(parent, parents1)

		# Test removal
		self.assertIn(node3, parents1)

		node1.removeConnectionTo(node3)
		parents1 = [connection.getParent() for connection in connections1]

		self.assertNotIn(node3, parents1)

		connection1to2 = connections1[0]

		self.assertEqual(node1, connection1to2.getChild())
		self.assertEqual(node2, connection1to2.getParent())

		node1.removeConnection(connection1to2)

		self.assertEqual(len(connections1), 0)

	def test_nodeValuesAndFinalize(self):
		node1, node2 = self.nodes[0], self.nodes[1]

		# One parent
		node2.setName("Likes fruit")
		node2.addValue("Yes")
		node2.addValue("No")
		node1.setName("Likes bananas")
		node1.addValue("Yes")
		node1.addValue("No")

		node1.addParent(node2)
		node1.finalize()
		node1.definalize()

		# Two parents
		node3 = self.nodes[2]
		node3.setName("Likes woman")
		node3.addValue("Yes")
		node3.addValue("No")
		node3.addValue("Partially")

		node1.addParent(node3)
		node1.finalize()

	def test_utilityNode(self):
		node1, node2, node3 = self.nodes[0], self.nodes[1], self.nodes[2]
		util = UtilityNode(self.network)

		node1.setName("Has more than 1 million dollars")
		node1.setObservable(True)
		node1.addValue("Yes")
		node1.addValue("No")

		node2.setName("Winning a gamble of 2 million dollars")
		node2.setObservable(False)
		node2.addValue("Yes")
		node2.addValue("No")

		node3.setName("Has a keen eye for probability")
		node3.setObservable(True)
		node3.addValue("Yes")
		node3.addValue("No")

		node2.addParent(node3)

		util.addParent(node1)
		util.addParent(node2)

		node1.setCurrentValue("Yes")
		node2.setCurrentValue("No")
		node3.setCurrentValue("Yes")

		node3.finalize()
		node2.finalize()
		node1.finalize()

		util.finalize()
		print util.inferUtility()

	def test_networkValuesAndFinalize(self):
		# Make semi-complex network

		nodeNames = ["Likes hot weather", "Likes bananas", "Likes tropical climate", "Likes women", "Likes partying", "Likes donuts", "Wants to travel to: "]
		nodeValues = 3

	def test_nodeSizes(self):
		self.lol = 4

	def test_quadTreeInsertAndRetrieve(self):
		self.lol = 3

	def test_mapManagerSelectsCorrectNodes(self):
		self.lol = 3