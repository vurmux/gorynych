import uuid
from datetime import datetime

class Entity(object):
    """Basic class for all node objects"""
    def __init__(self, name, attributes={}, tags=set([])):
        super(Entity, self).__init__()
        self.uuid = uuid.uuid4()
        self.creation_time = datetime.now()
        self.last_modified_time = datetime.now()
        self.description = ""
        self.label = ""
        self.name = name
        self.tags = tags
        self.attributes = attributes
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_tags(self):
        return self.tags

    def add_tag(self, tag):
        self.tags.add(tag)

    def get_attributes(self):
        return self.attributes