from ...edge import Edge

class Includes(Edge):
    """Includes link"""

    meta = {
        "ontology": "gch",
        "typename": "Includes",
        "hierarchy": "gch/Entity.Edge.Includes"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Includes, self).__init__(attributes, tags)