from ...edge import Edge

class Containment(Edge):
    """Containment link"""

    meta = {
        "ontology": "gch",
        "typename": "Containment",
        "hierarchy": "gch/Entity.Edge.Containment"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Containment, self).__init__(attributes, tags)