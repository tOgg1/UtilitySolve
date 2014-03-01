from Misc import *
import pygame

class QTree:
	max = 16

	def __init__(self, rect = None):
		self.children = []
		self.predecessorNodes = []
		self.expanded = False

		if not isinstance(rect, pygame.Rect):
			raise ValueError('Rect input to this QuadTree-implementation has to be a pygame.Rect')
		self.rect = rect

	def insert(child):
		if not (self.contains(child)):
			return

		if(len(children) < max):
			self.children.append(child)
			return
		else:
			if not expanded:
				self.expand()
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

	def expand(self):

		if self.expanded:
			er("QTree-Node already expanded")

		# Top-left
		self.predecessorNodes[0] = QTree(pygame.Rect(self.rect.left,	self.rect.top,
										 		   	 self.rect.width/2, self.rect.height/2))
		# Top-right
		self.predecessorNodes[1] = QTree(pygame.Rect(self.rect.left + self.rect.width/2,
													 self.rect.top, self.rect.width/2,
													 self.rect.height/2))
		# Bottom-left
		self.predecessorNodes[2] = QTree(pygame.Rect(self.rect.left, self.rect.top + self.rect.height/2,
												     self.rect.width/2, self.rect.height/2))
		# Bottom-right
		self.predecessorNodes[3] = QTree(pygame.Rect(self.rect.left + self.rect.width/2,
												     self.rect.top 	+ self.rect.height/2,
													 self.rect.width/2,	self.rect.height/2))
		self.expanded = True

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
