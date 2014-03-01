class BayesianNetwork:

	def __init__(self, mapManager, root = None):
		self.nodes = []
		self.mapManager = mapManager
		self.name = "DefaultNetwork"
		self.root = root
		self.hasRoot = False

		if(self.nodes == None):
			return
		for node in self.nodes:
			self.nodes.append(node)

	def setRoot(root):
		self.root = root
		self.hasRoot = True

	def setName(self, name):
		self.name = name

	def addNode(self, node):
		self.nodes.append(node)
		self.mapManager.addNode(node)

	def finalize():
		for node in self.nodes:
			node.finalize()

	def definalize():
		for node in self.nodes:
			node.definalize()

	def getNodes():
		return self.nodes

	def getNodeList():
		return self.nodes

