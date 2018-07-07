from .basic.data import Data

class Email(Data):
    """docstring for Email"""

    meta = {
        "ontology": "gch",
        "typename": "Email",
        "hierarchy": "gch/Entity.Node.Data.Email"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Email, self).__init__(attributes, tags)
        self.add_attributes(
            "nickname",
            "domain"
        )
        email_string = "{}@{}".format(
            self.get_attr("nickname"),
            self.get_attr("domain")
        )
        self.set_attributes(
            name=email_string,
            label=email_string
        )
        self.set_attributes(**attributes)