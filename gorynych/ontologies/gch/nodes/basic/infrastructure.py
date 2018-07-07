from gorynych.core.node import Node

class Infrastructure(Node):
    """docstring for Infrastructure"""

    meta = {
        "ontology": "gch",
        "typename": "Infrastructure",
        "hierarchy": "gch/Entity.Node.Infrastructure"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Infrastructure, self).__init__(attributes, tags)
