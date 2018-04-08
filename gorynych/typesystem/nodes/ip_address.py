from .basic.data import Data

class IPAddress(Data):
    """docstring for IPAddress"""

    TYPE = "IP Address"

    def __init__(self, attributes={}, tags=set([])):
        super(IPAddress, self).__init__(attributes, tags)
        self.add_attributes(
            "ip"
        )
        self.set_attributes(
            name=self.get_attr("ip"),
            label=self.get_attr("ip")
        )
        self.set_attributes(**attributes)