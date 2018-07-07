from gorynych.core.edge import Edge

class Aggregation(Edge):
    """Aggregation link"""

    meta = {
        "ontology": "gch",
        "typename": "Aggregation",
        "hierarchy": "gch/Entity.Edge.Aggregation"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Aggregation, self).__init__(attributes, tags)