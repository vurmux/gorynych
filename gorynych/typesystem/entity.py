import uuid
from datetime import datetime

class Entity(object):
    """Basic class for all entity objects"""

    meta = {
        "ontology": "gch",
        "typename": "Entity"
        "hierarchy": "gch/Entity"
    }

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

    def fuse(self, other, conflict="rename_other"):
        """
        Fuse another entity to current entity
        """

        # TODO: Fuse zope interfaces (after they will be implemented)

        # TODO: Change the class of the current entity if
        #       the other entity is the subtype of the current
        if not (self.meta.hierarchy.startswith(other.meta.hierarchy) or
                other.meta.hierarchy.startswith(self.meta.hierarchy)):
            raise Exception("Cannot fuse nodes: they are not in subclass-superclass relations")

        current_attrs = set(self.attrs.keys())
        other_attrs = set(other.attrs.keys())

        conflict_attrs = current_attrs & other_attrs
        for attr in conflict_attrs:
            if self.attrs[attr] != other.attrs[attr]:
                now = str(int(datetime.timestamp(datetime.now())))
                if conflict == 'keep_self':
                    pass
                elif conflict == 'keep_other':
                    self.attrs[attr] = other.attrs[attr]
                elif conflict == 'rename_self':
                    self.attrs[attr+'_'+now] = self.attrs[attr]
                    self.attrs[attr] = other.attrs[attr]
                elif conflict == 'rename_other':
                    self.attrs[attr+'_'+now] = other.attrs[attr]
                else:
                    raise AttributeError("Incorrect conflict value")

        attrs_to_add = other_attrs - current_attrs
        for attr in attrs_to_add:
            self.attrs[attr] = other.attrs[attr]