#!/usr/bin/python3


import json

import daemon

from gorynych import scheduler
from gorynych import overseer


ovsr = overseer.Overseer()
ovsr.load_scarabs()
sdlr = scheduler.Scheduler(ovsr)

with daemon.DaemonContext():
    sdlr.run()
