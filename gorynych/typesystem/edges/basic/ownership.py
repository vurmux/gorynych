from ...edge import Edge

class Ownership(Edge):
    """Ownership link"""

    TYPE = "Ownership"

    def __init__(self, attributes={}, tags=set([])):
        super(Ownership, self).__init__(attributes, tags)