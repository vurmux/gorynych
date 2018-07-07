from gorynych.core.edge import Edge

class Membership(Edge):
    """Membership link"""

    meta = {
        "ontology": "gch",
        "typename": "Membership",
        "hierarchy": "gch/Entity.Edge.Membership"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Membership, self).__init__(attributes, tags)