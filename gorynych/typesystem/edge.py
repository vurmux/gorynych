import uuid
from datetime import datetime

from .entity import Entity

class Edge(Entity):

    TYPE = "Edge"

    """Basic class for all edge objects"""
    def __init__(self, attributes={}, tags=set([])):
        super(Edge, self).__init__(attributes, tags)
