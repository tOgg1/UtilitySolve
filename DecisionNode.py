from BayesianNode import BayesianNode

class DecisionNode(BayesianNode):

	def __init__(self):
		super.__init__(self)

	def finalize(self):
		er("Can not finalize a decision node")
		return