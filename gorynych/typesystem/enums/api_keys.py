from enum import Enum, unique

@unique
class ApiKeys(Enum):
    google = 1
    yandex = 2
    bing = 3
    shodan = 4