from ...node import Node

class Location(Node):
    """docstring for Location"""

    meta = {
        "ontology": "gch",
        "typename": "Location",
        "hierarchy": "gch:Entity.Node.Location"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Location, self).__init__(attributes, tags)
