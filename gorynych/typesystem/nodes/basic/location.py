from ...node import Node

class Location(Node):
    """docstring for Location"""

    meta = {
        "ontology": "gch",
        "typename": "Location",
        "hierarchy": "gch:Entity.Node.Location"
    }

    def __init__(self, name):
        super(Location, self).__init__(name)
