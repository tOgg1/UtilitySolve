class QTree:
	max = 16

	def __init__(self, rect = None):
		self.children = []
		self.predecessorNodes = []
		self.rect = rect

	def insert(child):
		if not (self.contains(child)):
			return

		if(len(children) < max):
			self.children.append(child)
			return
		else:
			for node in self.predecessorNodes:
				node.insert(child)

	def remove(possibleChild):
		for child in children:
			if(child == possibleChild):
				self.children.remove(child)
				return

		for node in predecessorNodes:
			node.remove(possibleChild)

	def contains(child, rect = None):
		return rect.contains(child.getRect())

	def getChildrenInRegion(region):
		validChildren = []

		for child in self.children:
			if(region.contains(child.getRect())):
				validChildren.append(child)

		for node in predecessorNodes:
			validChildren.extend(node.getChildrenInRegion(region))

	def getAllChildren():
		validChildren = []

		validChildren.extend(self.children)

		for node in predecessorNodes:
			validChildren.extend(node.getAllChildren())

		return validChildren
