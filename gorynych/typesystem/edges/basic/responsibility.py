from ...edge import Edge

class Responsibility(Edge):
    """Responsibility link"""

    TYPE = "Responsibility"

    def __init__(self, attributes={}, tags=set([])):
        super(Responsibility, self).__init__(attributes, tags)