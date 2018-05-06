from ..core.module import Module
from ..core.constants import *


class DumbModule(Module):
    # Module metainfo
    meta = {
        "name": "Dumb module",
        "author": "",
        "supertype": GCH_MODULE_SUPERTYPE_SCRIPT,
        "type": GCH_MODULE_TYPE_SCRAPER,
        "required_keys": [],
        "short_description": "",
        "long_description": "",
        "tags": []
    }

    def run(*args, **kwargs):
        print("I am the dumb module!")

if __name__ == "__main__":
    dumb_module = DumbModule()
    dumb_module.run()