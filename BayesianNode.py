from PyGameHelpers import *

class BayesianNode:

	image = None
	imageRect = None
	imageHighlighted = None
	imageHighlightedRect = None
	imageConnection = None
	imageConnectionRect = None

	@staticmethod
	def loadImages(setSize = None):
		BayesianNode.image, BayesianNode.imageRect = loadImage("circle.png")
		BayesianNode.imageHighlighted, BayesianNode.imageHighlightedRect = loadImage("circle_highlighted.png")
		#BayesianNode.imageConnection, BayesianNode.imageConnectionRect = loadImage("arrow.png")		


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
