class BayesianNetwork:

	def __init__(self, mapManager, nodes = None):
		self.nodes = []
		self.mapManager = mapManager

		if(nodes == None):
			return
		for node in nodes:
			self.nodes.append(node)

	def addNode(self, node):
		self.nodes.append(node)
		self.mapManager.addNode(node)

	def finalize():
		for node in self.nodes:
			node.finalize()

	def getNodes():
		return self.nodes