#!/usr/bin/python3


import time

import schedule


class Scheduler(object):

    def __init__(self, overseer):
        self.overseer = overseer
        self.scheduler = schedule.Scheduler()
        self.jobs = []
        self.init_jobs()

    def init_jobs(self):
        for scarab in self.overseer.get_scarabs_names():
            self.scheduler.every().minute.do(
                lambda: self.overseer.run_scarab(scarab)
            )

    def run(self):
        while True:
            self.scheduler.run_pending()
            time.sleep(1)
