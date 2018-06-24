from .data import Data

class Document(Data):
    """docstring for Document"""

    meta = {
        "ontology": "gch",
        "typename": "Document",
        "hierarchy": "gch/Entity.Node.Data.Document"
    }

    def __init__(self, name):
        super(Document, self).__init__(name)