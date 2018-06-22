from ...node import Node

class Agent(Node):
    """docstring for Agent"""

    meta = {
        "ontology": "gch",
        "typename": "Agent"
        "hierarchy": "gch/Entity.Node.Agent"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Agent, self).__init__(attributes, tags)

