#!/usr/bin/python3


import json

import daemon

from gorynych import scheduler
from gorynych import overseer


# TODO: Change config place to default
with open('./config.json') as config_file:
    config = json.loads(config_file.read())
    overseer.load_scarabs(config)
    scheduler.init(config)
with daemon.DaemonContext():
    scheduler.run()
