from ...node import Node

class Data(Node):
    """docstring for Data"""

    meta = {
        "ontology": "gch",
        "typename": "Data",
        "hierarchy": "gch/Entity.Node.Data"
    }

    def __init__(self, name):
        super(Data, self).__init__(name)
