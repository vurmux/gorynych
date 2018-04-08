from ...edge import Edge

class Usage(Edge):
    """Usage link"""

    TYPE = "Usage"

    def __init__(self, attributes={}, tags=set([])):
        super(Usage, self).__init__(attributes, tags)