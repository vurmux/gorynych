from ...node import Node

class Event(Node):
    """docstring for Event"""

    meta = {
        "ontology": "gch",
        "typename": "Event",
        "hierarchy": "gch/Entity.Node.Event"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Event, self).__init__(attributes, tags)