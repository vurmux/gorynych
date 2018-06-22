from ...edge import Edge

class Connection(Edge):
    """Connection link"""

    meta = {
        "ontology": "gch",
        "typename": "Connection"
        "hierarchy": "gch/Entity.Edge.Connection"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Connection, self).__init__(attributes, tags)