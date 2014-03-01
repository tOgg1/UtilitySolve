from BayesianNode import BayesianNode
from Misc import normalPrint as pr, errorPrint as er
from Misc import *

class UtilityNode(BayesianNode):

	def __init__(self, network = None):
		BayesianNode.__init__(self, network)
		self.CPT = None
		self.utilityTable = []

	def finalize(self):
		if(self.network == None):
			er("Can't finalize (any) node which is not a part of a network")
			return

		for parent in self.parents:
			if not parent.finalized == True:
				er("Parent is not finalized, what are you doing?! Exiting ...")
				return
			for value in parent.getValues():
				pr("Please specify utility for " + str(parent.getName()) + " = " + str(value))
				ans = parseInputToNumber(input("Answer: "))
				self.utilityTable.append(([parent, value], ans))

	def inferUtility(self):
		if(self.network == None):
			er("Can't give the utility of a node not part of a network")

		utility = 0
		for parent in self.parents:
			curValueForParent = parent.getCurrentValue()

			for utilityTuple in self.utilityTable:
				if(utilityTuple[0][0] == parent and utilityTuple[0][1] == curValueForParent):
					utility += utilityTuple[1]

		return utility


