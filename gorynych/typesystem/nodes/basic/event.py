from ...node import Node

class Event(Node):

    TYPE = "Event"

    """docstring for Event"""
    def __init__(self, name):
        super(Event, self).__init__(name)