from .group import Group

class Organization(Group):

    TYPE = "Organization"

    """docstring for Organization"""
    def __init__(self, attributes={}, tags=set([])):
        super(Organization, self).__init__(attributes, tags)
        self.add_attributes(
            "name",
            "foundation_date"
        )
        self.set_attributes(**attributes)