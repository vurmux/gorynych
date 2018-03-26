import uuid
from datetime import datetime

from .entity import Entity

class Node(Entity):
    """Basic class for all node objects"""
    def __init__(self, name, attributes={}, tags=set([])):
        super(Node, self).__init__(name, attributes, tags)
