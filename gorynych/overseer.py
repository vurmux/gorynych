#!/usr/bin/python3


import os
import sys
import json
import imp
import inspect
import time
import codecs
from pkg_resources import resource_string


class Overseer(object):

    def __init__(self):
        raw_config = resource_string(__name__, 'config.json')
        raw_config = raw_config.decode('utf-8').replace('<HOME>', os.environ['HOME'])
        config = json.loads(raw_config)
        self.config = config
        self.scarabs = {}

    def load_config(self, config):
        self.config = config

    def load_folder(self, folder):
        for (dirpath, dirnames, filenames) in os.walk(folder):
            for filename in filenames:
                if filename == '__init__.py':
                    continue
                full_path = dirpath + filename
                if filename.find('.') != -1:
                    name, filetype = filename.rsplit('.', 1)
                else:
                    name = filename
                    filetype = None
                module = imp.load_module(
                    name,
                    *imp.find_module(name, [dirpath])
                )
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
                scarab_config = {}
                try:
                    with open(
                            '{}/{}.json'.format(dirpath, name)
                    ) as scarab_config_file:
                        scarab_config = json.loads(scarab_config_file.read())
                except FileNotFoundError:
                    scarab_config = {}
                for scarab in raw_scarabs_classes_list:
                    self.scarabs[scarab[0]] = scarab[1](**scarab_config)

    def load_scarabs(self):
        self.load_folder(self.config["default_scarabs_folder"])
        for folder in self.config["additional_scarabs_folders"]:
            self.load_folder(folder)

    def get_scarabs(self):
        return self.scarabs

    def get_scarabs_names(self):
        return set(self.scarabs.keys())

    def run_scarab(self, scarab_name):
        # TODO: Add another types of information storing (memory etc.)
        current_time = time.gmtime()
        result_filename = "{}_{}-{}-{}_{}-{}-{}GM".format(
            scarab_name,
            current_time.tm_year,
            current_time.tm_mon,
            current_time.tm_mday,
            current_time.tm_hour,
            current_time.tm_min,
            current_time.tm_sec,
        )
        with codecs.open(
                self.config["default_output_folder"] + '/' + result_filename,
                mode='w',
                encoding='utf-8'
        ) as result_file:
            for result in self.scarabs[scarab_name].run_default():
                result_file.write(str(result))


if __name__ == '__main__':
    overseer = Overseer()
    overseer.load_scarabs()
    print(overseer.scarabs)
