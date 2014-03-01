from BayesianNode import BayesianNode

class DecisionNode(BayesianNode):

	def __init__(self):
		super.__init__(self)

	def finalize(self):
		finalized = True
		return

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setNetwork(self, network):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform setNetwork.")
			return
		self.network = network

	def addValue(self, value):
		if(self.finalized):
			er("[Node]: Node is already finalized. Can not perform addValue.")
			return
		self.values.append(value)

	def getValues(self):
		return self.values

	def getCurrentValue(self):
		er("[DecisionNode]: This is a DecisionNode....")

	def setCurrentValue(self, value):
		er("[DecisionNode]: This is a DecisionNode....")

	def addParent(self, parent):
		er("[DecisionNode]: This is a DecisionNode....")

	def addParents(self, parents):
		er("[DecisionNode]: This is a DecisionNode....")
	
	def removeParent(self, parent):
		er("[DecisionNode]: This is a DecisionNode....")

	def getParents(self):
		er("[DecisionNode]: This is a DecisionNode....")
	
	def getListPossibleValues(self, cpt, i, j, rootTuple, currentSetValues, remainingList):
		er("[DecisionNode]: This is a DecisionNode....")

	def definalize(self):
		er("[DecisionNode]: This is a DecisionNode....")
	
	def setObservable(self, boolean):
		er("[DecisionNode]: This is a DecisionNode....")

	def getProbabilityOfValue(self, value):
		return 1	

	def getProbabilityOfTuple(self, value):
		return 1
	
	def addConnection(self, connection):
		er("[DecisionNode]: This is a DecisionNode....")

	def removeConnection(self, connection):
		er("[DecisionNode]: This is a DecisionNode....")

	def removeConnectionTo(self, parent):
		er("[DecisionNode]: This is a DecisionNode....")


	def getConnections(self):
		return self.connections

