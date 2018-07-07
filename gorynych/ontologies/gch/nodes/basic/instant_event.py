from .event import Event

class InstantEvent(Event):
    """docstring for Instant event"""

    meta = {
        "ontology": "gch",
        "typename": "Instant event",
        "hierarchy": "gch/Entity.Node.Event.InstantEvent"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(InstantEvent, self).__init__(attributes, tags)
        self.add_attributes(
            "timestamp"
        )
        self.set_attributes(**attributes)