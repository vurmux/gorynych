from ...node import Node

class Group(Node):
    """docstring for Group"""

    meta = {
        "ontology": "gch",
        "typename": "Group"
        "hierarchy": "gch/Entity.Node.Group"
    }

    def __init__(self, name):
        super(Group, self).__init__(name)
