class BayesianNetwork:

	def __init__(self, nodes = None):
		self.nodes = []

		if(nodes == None):
			return
		for node in nodes:
			self.nodes.append(node)

	def addNode(self, node):
		self.nodes.append(node)

	def finalize():
		for node in self.nodes:
			node.finalize()

	def buildVisual():
		hei = 2
		# Create minimal bounding box for entire system

		# Determine root-nodes

		# Place nodes in relative-coordinates

		# Place nodes on screen