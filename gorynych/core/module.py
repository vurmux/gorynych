#!/usr/bin/python3


import pickle
from abc import ABCMeta, abstractmethod
import re
import os.path
from datetime import datetime
import json

from .constants import *


class Module(metaclass=ABCMeta):
    """
    Abstract base class for all modules.
    """

    # Module metainfo
    meta = {
        "name": "",
        "author": "",
        "supertype": None,
        "type": None,
        "required_keys": [],
        "short_description": "",
        "long_description": "",
        "tags": []
    }

    options = {}

    def __init__(self):
        # Module state: used for the saving/restoring the module.
        # All temporary info should be stored here.
        self._state = {}

        # API keys
        self._api_keys = {}

        # Module working directory
        self._working_directory = None

        # Current extracted graph
        self._current_graph = None

        # Load configuration info from the config.json if the module's
        # supertype is `folder`
        if self.meta["supertype"] == GCH_MODULE_SUPERTYPE_FOLDER:
            with open("config.json", "r") as config_file:
                config = json.loads(config_file.read())
                self.options = config["options"]

    def _save_state(self):
        pass

    def _load_state(self, state):
        pass

    def _dump(self, filename):
        pickle.dump(self, os.path.join(self._working_directory, filename))

    def _get_required_keys(self):
        pass

    def get_meta(self):
        return self.meta

    def freeze(self):
        filename = "dump-{}.tmp".format(
            datetime.strftime(datetime.utcnow(), "%Y%m%d%H%M%S")
        )
        self._dump(filename)

    def restore(self, file):
        pass

    @abstractmethod
    def run(*args, **kwargs):
        pass
