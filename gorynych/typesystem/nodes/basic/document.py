from .data import Data

class Document(Data):

    TYPE = "Document"

    """docstring for Document"""
    def __init__(self, name):
        super(Document, self).__init__(name)