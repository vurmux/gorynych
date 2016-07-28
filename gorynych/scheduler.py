#!/usr/bin/python3


import time
import sched

from gorynych.task import Task


class Scheduler(object):

    def __init__(self, overseer):
        self.overseer = overseer
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.__tasks = {}

    def create_task(self, task):
        self.__tasks[task.name] = task

    def run_task(self, task_name, priority=0):
        self.scheduler.enter(0, priority, lambda: self.__tasks[task_name].run())
        # Scheduler stops when it's queue is empty. This code forces it to run.
        if len(self.scheduler.queue) == 1:
            self.scheduler.run(blocking=False)

    def run_all(self):
        pass

    def launch(self):
        self.scheduler.run(blocking=False)
