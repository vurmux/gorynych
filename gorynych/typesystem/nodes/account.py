from .basic.data import Data

class Account(Data):
    """docstring for Account"""

    meta = {
        "ontology": "gch",
        "typename": "Account"
        "hierarchy": "gch/Entity.Node.Data.Account"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Account, self).__init__(attributes, tags)
        self.add_attributes(
            "nickname",
            "domain"
        )
        self.set_attributes(**attributes)