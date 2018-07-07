from .event import Event

class ContiniousEvent(Event):
    """docstring for Continious event"""

    meta = {
        "ontology": "gch",
        "typename": "Continious event",
        "hierarchy": "gch/Entity.Node.Event.ContiniousEvent"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(ContiniousEvent, self).__init__(attributes, tags)
        self.add_attributes(
            "start_timestamp",
            "end_timestamp"
        )
        self.set_attributes(**attributes)