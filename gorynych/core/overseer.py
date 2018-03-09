#!/usr/bin/python3


import os
import json
from imp import load_module, find_module
from inspect import getmembers, isclass
import time
import codecs
from pkg_resources import resource_string


class Overseer(object):

    def __init__(self):
        raw_config = resource_string(__name__, 'config.json')
        raw_config = raw_config.decode('utf-8').replace('<HOME>', os.environ['HOME'])
        config = json.loads(raw_config)
        self.config = config
        self._scarabs = {}

    @property
    def scarabs(self):
        return self._scarabs

    def get_scarab(self, scarab_name):
        if scarab_name in self._scarabs:
            return self._scarabs[scarab_name]
        return None

    def list_scarabs(self):
        return list(self._scarabs.keys())
    
    def load_config(self, config):
        self.config = config

    def load_folder(self, folder):
        for (dirpath, dirnames, filenames) in os.walk(folder):
            for filename in filenames:
                name, filetype = (
                    filename.rsplit('.', 1)
                    if filename.find('.') != -1
                    else (filename, None)
                )
                if filename == '__init__.py':
                    continue
                if filetype != 'py':
                    continue
                module = load_module(name, *find_module(name, [dirpath]))
                raw_scarabs_classes = getmembers(
                    module,
                    lambda m: (
                        (hasattr(m, '__module__') and m.__module__ == name) and
                        isclass(m)
                    )
                )
                for scarab in raw_scarabs_classes:
                    self._scarabs[scarab[0]] = scarab[1]()

    def load_scarabs(self):
        self.load_folder(self.config['default_scarabs_folder'])
        for folder in self.config['additional_scarabs_folders']:
            self.load_folder(folder)

    def run_scarab(self, scarab_name):
        # TODO: Add another types of information storing (memory etc.)
        current_time = time.gmtime()
        filename = '{}_{}-{}-{}_{}-{}-{}GM'.format(
            scarab_name,
            current_time.tm_year,
            current_time.tm_mon,
            current_time.tm_mday,
            current_time.tm_hour,
            current_time.tm_min,
            current_time.tm_sec,
        )
        filepath = self.config['default_output_folder'] + '/' + filename
        with codecs.open(filepath, mode='w', encoding='utf-8') as result_file:
            for result in self._scarabs[scarab_name].run_default():
                result_file.write(str(result))


if __name__ == '__main__':
    overseer = Overseer()
    overseer.load_scarabs()
    print(overseer.scarabs)
