from enum import Enum, unique


# Module supertypes constants
GCH_MODULE_SUPERTYPE_SCRIPT = "gch_script"
GCH_MODULE_SUPERTYPE_FOLDER = "gch_folder"

GCH_MODULE_SUPERTYPES = set([
    GCH_MODULE_SUPERTYPE_SCRIPT,
    GCH_MODULE_SUPERTYPE_FOLDER
])


# Module types constants
GCH_MODULE_TYPE_SCRAPER = "gch_scraper"
GCH_MODULE_TYPE_HARVESTER = "gch_harvester"
GCH_MODULE_TYPE_LINKER = "gch_linker"
GCH_MODULE_TYPE_EXPORTER = "gch_exporter"

GCH_MODULE_TYPES = set([
    GCH_MODULE_TYPE_SCRAPER,
    GCH_MODULE_TYPE_HARVESTER,
    GCH_MODULE_TYPE_LINKER,
    GCH_MODULE_TYPE_EXPORTER
])


# API keys enum
@unique
class ApiKeys(Enum):
    google = 1
    yandex = 2
    bing = 3
    shodan = 4