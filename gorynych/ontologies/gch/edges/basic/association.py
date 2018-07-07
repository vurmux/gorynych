from gorynych.core.edge import Edge

class Association(Edge):
    """Association link"""

    meta = {
        "ontology": "gch",
        "typename": "Association",
        "hierarchy": "gch/Entity.Edge.Association"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Association, self).__init__(attributes, tags)