from .event import Event

class ContiniousEvent(Event):

    TYPE = "Continious event"

    """docstring for Continious event"""
    def __init__(self, name):
        super(ContiniousEvent, self).__init__(name)
        self.add_attributes(
            "start_timestamp",
            "end_timestamp"
        )
        self.set_attributes(**attributes)