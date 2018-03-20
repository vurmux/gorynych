from .agent import Agent

class Person(Agent):
    """docstring for Person"""
    def __init__(self, name, full_name="", nationality=None,
            date_of_birth=None, alternative_names=[], aliases=[]):
        super(Person, self).__init__(name)
        self.full_name = full_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.alternative_names = alternative_names
        self.aliases = aliases