from ...edge import Edge

class Dependency(Edge):
    """Dependency link"""

    meta = {
        "ontology": "gch",
        "typename": "Dependency",
        "hierarchy": "gch/Entity.Edge.Dependency"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Dependency, self).__init__(attributes, tags)