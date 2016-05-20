#!/usr/bin/python3


import json
import os

import daemon

import scheduler
import overseer


ovsr = overseer.Overseer()
ovsr.load_scarabs()
sdlr = scheduler.Scheduler(ovsr)

#daemon_options = {
#    'working_directory': os.environ["HOME"] + '/.gorynych',
#    'umask': 0o002
#}

#with daemon.DaemonContext(**daemon_options):
sdlr.run()
