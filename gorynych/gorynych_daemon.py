#!/usr/bin/python3


import json
import os

import daemon

from gorynych import scheduler
from gorynych import overseer


ovsr = overseer.Overseer()
ovsr.load_scarabs()
sdlr = scheduler.Scheduler(ovsr)

#daemon_options = {
#    'working_directory': os.environ["HOME"] + '/.gorynych',
#    'umask': 0o002
#}

#with daemon.DaemonContext(**daemon_options):

def main():
    sdlr.run()

if __name__ == '__main__':
    main()
