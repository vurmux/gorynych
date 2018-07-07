from .entity import Entity

class Edge(Entity):
    """Basic class for all edge objects"""

    meta = {
        "ontology": "gch",
        "typename": "Edge",
        "hierarchy": "gch/Entity.Edge"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Edge, self).__init__(attributes, tags)
