from ...edge import Edge

class Connection(Edge):
    """Connection link"""

    TYPE = "Connection"

    def __init__(self, attributes={}, tags=set([])):
        super(Connection, self).__init__(attributes, tags)