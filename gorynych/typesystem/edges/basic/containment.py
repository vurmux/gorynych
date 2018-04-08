from ...edge import Edge

class Containment(Edge):
    """Containment link"""

    TYPE = "Containment"

    def __init__(self, attributes={}, tags=set([])):
        super(Containment, self).__init__(attributes, tags)