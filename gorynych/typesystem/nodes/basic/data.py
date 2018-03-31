from ...node import Node

class Data(Node):

    TYPE = "Data"

    """docstring for Data"""
    def __init__(self, name):
        super(Data, self).__init__(name)
