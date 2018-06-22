from ...edge import Edge

class Usage(Edge):
    """Usage link"""

    meta = {
        "ontology": "gch",
        "typename": "Usage"
        "hierarchy": "gch/Entity.Edge.Usage"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Usage, self).__init__(attributes, tags)