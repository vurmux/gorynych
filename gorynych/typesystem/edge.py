import uuid
from datetime import datetime

from .entity import Entity

class Edge(Entity):
    """Basic class for all edge objects"""
    def __init__(self, name, attributes={}, tags=set([])):
        super(Edge, self).__init__(name, attributes, tags)
