from ...edge import Edge

class Membership(Edge):
    """Membership link"""

    TYPE = "Membership"

    def __init__(self, attributes={}, tags=set([])):
        super(Membership, self).__init__(attributes, tags)