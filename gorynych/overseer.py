#!/usr/bin/python3


import os
import sys
import json
import imp
import inspect


class Overseer(object):

    def __init__(self, config):
        self.config = config
        self.scarabs = []

    def load_config(self, config):
        self.config = config

    def load_folder(folder):
        for (dirpath, dirnames, filenames) in os.walk():
            for filename in filenames:
                full_path = dirpath + filename
                filetype = filename.split('.')[-1]
                if filetype == 'py':
                    # FIXME: bad code
                    name = filename[-3]
                    module = imp.load_module(name, *imp.find_module(name))
                    raw_scarabs_classes_list = inspect.getmembers(
                        module,
                        lambda member: (
                            (
                                hasattr(member, '__module__') and
                                member.__module__ == name
                            ) and
                            inspect.isclass(member)
                        )
                    )
                    with open(name + '.json') as scarab_config_file:
                        scarab_config = json.loads(scarab_config_file.read())
                    for scarab in raw_scarabs_classes_list:
                        self.scarabs.append(scarab[1](**scarab_config))
                # TODO: use imp.get_magic()
                elif filetype == 'pyc':
                    pass

    def load_scarabs(self):
        self.load_folder(self.config["default_scarabs_folder"])
        for folder in self.config["additional_scarabs_folders"]:
            self.load_folder(folder)
