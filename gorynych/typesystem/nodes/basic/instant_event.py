from .event import Event

class InstantEvent(Event):

    TYPE = "Instant event"

    """docstring for Instant event"""
    def __init__(self, name):
        super(InstantEvent, self).__init__(name)
        self.add_attributes(
            "timestamp"
        )
        self.set_attributes(**attributes)