from ...node import Node

class Agent(Node):

    TYPE = "Agent"

    """docstring for Agent"""
    def __init__(self, attributes={}, tags=set([])):
        super(Agent, self).__init__(attributes, tags)

