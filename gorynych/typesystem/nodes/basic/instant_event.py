from .event import Event

class InstantEvent(Event):
    """docstring for Instant event"""

    meta = {
        "ontology": "gch",
        "typename": "Instant event"
        "hierarchy": "gch/Entity.Node.Event.InstantEvent"
    }

    def __init__(self, name):
        super(InstantEvent, self).__init__(name)
        self.add_attributes(
            "timestamp"
        )
        self.set_attributes(**attributes)