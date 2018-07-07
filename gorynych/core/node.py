import uuid
from datetime import datetime

from .entity import Entity

class Node(Entity):
    """Basic class for all node objects"""

    meta = {
        "ontology": "gch",
        "typename": "Node",
        "hierarchy": "gch/Entity.Node"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Node, self).__init__(attributes, tags)
