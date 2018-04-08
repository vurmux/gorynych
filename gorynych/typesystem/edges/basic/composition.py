from ...edge import Edge

class Composition(Edge):
    """Composition link"""

    TYPE = "Composition"

    def __init__(self, attributes={}, tags=set([])):
        super(Composition, self).__init__(attributes, tags)