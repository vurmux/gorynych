from ...edge import Edge

class Association(Edge):
    """Association link"""

    TYPE = "Association"

    def __init__(self, attributes={}, tags=set([])):
        super(Association, self).__init__(attributes, tags)