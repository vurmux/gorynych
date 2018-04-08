from .basic.data import Data

class Nickname(Data):
    """docstring for Nickname"""

    TYPE = "Nickname"

    def __init__(self, attributes={}, tags=set([])):
        super(Nickname, self).__init__(attributes, tags)
        self.add_attributes(
            "nickname"
        )
        self.set_attributes(
            name=self.get_attr("nickname"),
            label=self.get_attr("nickname")
        )
        self.set_attributes(**attributes)