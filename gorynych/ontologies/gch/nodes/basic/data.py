from gorynych.core.node import Node

class Data(Node):
    """docstring for Data"""

    meta = {
        "ontology": "gch",
        "typename": "Data",
        "hierarchy": "gch/Entity.Node.Data"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Data, self).__init__(attributes, tags)
