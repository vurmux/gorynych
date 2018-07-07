from gorynych.core.edge import Edge

class Composition(Edge):
    """Composition link"""

    meta = {
        "ontology": "gch",
        "typename": "Composition",
        "hierarchy": "gch/Entity.Edge.Composition"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Composition, self).__init__(attributes, tags)