from ...edge import Edge

class Aggregation(Edge):
    """Aggregation link"""

    TYPE = "Aggregation"

    def __init__(self, attributes={}, tags=set([])):
        super(Aggregation, self).__init__(attributes, tags)