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
        #TODO: Really? Looks like bad code!
        self.__tasks[task.name].scheduler = self

    def delete_task(self, task_name):
        pass

    def run_task(self, task_name, priority=0):
        self.scheduler.enter(0, priority, lambda: self.__tasks[task_name].run())
        # Scheduler stops when it's queue is empty. This code forces it to run.
        if len(self.scheduler.queue) == 1:
            self.scheduler.run(blocking=False)

    def run_all(self):
        for task in self._tasks:
            self.run_task(task)

    def launch(self):
        self.scheduler.run(blocking=False)

    @property
    def tasks(self):
        pass

    @property
    def inactive_tasks(self):
        pass

    @property
    def active_tasks(self):
        pass

    @property
    def running_tasks(self):
        pass

    @property
    def paused_tasks(self):
        pass

    @property
    def aborted_tasks(self):
        pass

    @property
    def completed_tasks(self):
        pass

    @property
    def failed_tasks(self):
        pass

    @property
    def frozen_tasks(self):
        pass
