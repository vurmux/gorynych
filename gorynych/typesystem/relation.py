import uuid


class Relation(object):
    """Basic class for all relation objects"""
    def __init__(self, from_type, to_type, edge_type):
        self.from_type = from_type
        self.to_type = to_type
        self.edge_type = edge_type
        self.uuid = uuid.uuid4()
