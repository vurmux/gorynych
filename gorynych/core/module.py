#!/usr/bin/python3


import pickle
from abc import ABCMeta, abstractmethod
import re
import os.path
from datetime import datetime


class Module(metaclass=ABCMeta):
    """
    Abstract base class for all modules.
    """

    meta = {}

    def __init__(self):
        # Module state: used for the saving/restoring the module.
        # All temporary info should be stored here.
        self._state = {}
        self._working_directory = None

    def _save_state(self):
        pass

    def _load_state(self, state):
        pass

    def _dump(self, filename):
        pickle.dump(self, os.path.join(self._working_directory, filename))

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
