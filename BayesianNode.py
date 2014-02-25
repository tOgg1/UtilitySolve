class BayesianNode:
	def __init__(self):
		self.parents = []

		self.values = []
		self.CPT = {}

		self.finalized = False

	def addValue(self, value):
		values.append(value)

	def addParent(self, parent):
		self.parents.append(parent)

	def finalize(self):
		self.finalized = True

	def getProbability(parent, value):
		self.lol = true
