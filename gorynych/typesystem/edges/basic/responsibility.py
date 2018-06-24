from ...edge import Edge

class Responsibility(Edge):
    """Responsibility link"""

    meta = {
        "ontology": "gch",
        "typename": "Responsibility",
        "hierarchy": "gch/Entity.Edge.Responsibility"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Responsibility, self).__init__(attributes, tags)