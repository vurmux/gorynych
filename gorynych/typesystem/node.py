import uuid
from datetime import datetime

from .entity import Entity

class Node(Entity):

    TYPE = "Node"
    
    """Basic class for all node objects"""
    def __init__(self, attributes={}, tags=set([])):
        super(Node, self).__init__(attributes, tags)
