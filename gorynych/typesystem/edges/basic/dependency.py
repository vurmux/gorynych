from ...edge import Edge

class Dependency(Edge):
    """Dependency link"""

    TYPE = "Dependency"

    def __init__(self, attributes={}, tags=set([])):
        super(Dependency, self).__init__(attributes, tags)