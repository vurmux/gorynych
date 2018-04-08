from ...node import Node

class Infrastructure(Node):

    TYPE = "Infrastructure"

    """docstring for Infrastructure"""
    def __init__(self, name):
        super(Infrastructure, self).__init__(name)
