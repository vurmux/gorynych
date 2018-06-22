from .group import Group

class Organization(Group):
    """docstring for Organization"""

    meta = {
        "ontology": "gch",
        "typename": "Organization"
        "hierarchy": "gch/Entity.Node.Group.Organization"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Organization, self).__init__(attributes, tags)
        self.add_attributes(
            "name",
            "foundation_date"
        )
        self.set_attributes(**attributes)