from ProblemBuilder import *


# Class for testing
class TestClass(unittest.TestCase):

	def setUp(self):
		# Init core-objects
		self.mapManager = MapManager([200, 200])
		self.network = BayesianNetwork(self.mapManager)
		self.nodes = [BayesianNode() for i in range(1,10)]

	def test_baseFunctionality(self):
		self.assertEqual(self.mapManager, self.network.mapManager)
		self.assertEqua


	def test_quadTreeInsertAndRetrieve(self):
		self.lol = 3

cnf.testing = True
cnf.debug = True