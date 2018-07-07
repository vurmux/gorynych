from gorynych.core.edge import Edge

class Ownership(Edge):
    """Ownership link"""

    meta = {
        "ontology": "gch",
        "typename": "Ownership",
        "hierarchy": "gch/Entity.Edge.Ownership"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Ownership, self).__init__(attributes, tags)