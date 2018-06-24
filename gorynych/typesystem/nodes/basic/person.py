from .agent import Agent

class Person(Agent):
    """docstring for Person"""

    meta = {
        "ontology": "gch",
        "typename": "Person",
        "hierarchy": "gch/Entity.Node.Agent.Person"
    }

    def __init__(self, attributes={}, tags=set([])):
        super(Person, self).__init__(attributes, tags)
        self.add_attributes(
            "full_name",
            "nationality",
            "date_of_birth",
            "alternative_names",
            "aliases"
        )
        self.set_attributes(**attributes)