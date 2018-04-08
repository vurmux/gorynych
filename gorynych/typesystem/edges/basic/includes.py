from ...edge import Edge

class Includes(Edge):
    """Includes link"""

    TYPE = "Includes"

    def __init__(self, attributes={}, tags=set([])):
        super(Includes, self).__init__(attributes, tags)