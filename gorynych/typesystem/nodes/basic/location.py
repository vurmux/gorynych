from ...node import Node

class Location(Node):

    TYPE = "Location"

    """docstring for Location"""
    def __init__(self, name):
        super(Location, self).__init__(name)
