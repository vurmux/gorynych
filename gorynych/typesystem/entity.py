import uuid
from datetime import datetime

class Entity(object):
    """Basic class for all node objects"""

    TYPE = "Entity"

    def __init__(self, attributes={}, tags=set([])):
        super(Entity, self).__init__()
        self.uuid = uuid.uuid4()
        self.attributes = {
            "name": "",
            "label": "",
            "description": ""
        }
        if attributes and isinstance(attributes, dict):
            self.attributes = attributes
        self.creation_time = datetime.now()
        self.last_modified_time = datetime.now()
        self.tags = tags
    
    def get_name(self):
        return self.attributes["name"]

    def set_name(self, name):
        self.attributes["name"] = name

    def get_tags(self):
        return self.tags

    def add_tag(self, tag):
        self.tags.add(tag)

    def get_attribute(self, attr_name):
        return self.attributes[attr_name]

    def get_attr(self, attr_name):
        """
        Short alias for self.get_attribute()
        """
        return self.get_attribute(attr_name)

    def get_attributes(self):
        return self.attributes

    def add_attribute(self, attr_name, attr_value=None):
        if attr_name not in self.attributes:
            self.attributes[attr_name] = attr_value

    def add_attributes(self, *attr_names, **attr_names_values):
        for attr_name in attr_names:
            if str(attr_name) not in self.attributes:
                self.attributes[str(attr_name)] = None
        for attr_name in attr_names_values:
            if str(attr_name) not in self.attributes:
                self.attributes[str(attr_name)] = attr_value

    def set_attribute(self, attr_name, attr_value=None):
        if attr_name not in self.attributes:
            raise KeyError
        self.attributes[attr_name] = attr_value

    def set_attributes(self, **attributes):
        for attr in attributes:
            self.set_attribute(attr, attributes[attr])