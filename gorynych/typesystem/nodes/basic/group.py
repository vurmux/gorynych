from ...node import Node

class Group(Node):

    TYPE = "Group"

    """docstring for Group"""
    def __init__(self, name):
        super(Group, self).__init__(name)
