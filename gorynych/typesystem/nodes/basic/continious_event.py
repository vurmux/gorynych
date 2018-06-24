from .event import Event

class ContiniousEvent(Event):
    """docstring for Continious event"""

    meta = {
        "ontology": "gch",
        "typename": "Continious event",
        "hierarchy": "gch/Entity.Node.Event.ContiniousEvent"
    }

    def __init__(self, name):
        super(ContiniousEvent, self).__init__(name)
        self.add_attributes(
            "start_timestamp",
            "end_timestamp"
        )
        self.set_attributes(**attributes)