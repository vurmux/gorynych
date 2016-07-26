#!/usr/bin/python3


from enum import Enum


class State(Enum):
    inactive = 1
    active = 2
    running = 3
    paused = 4
    aborted = 5
    failed = 6
    frozen = 7


class Task(object):
 
    def __init__(self):
        self.state = State.inactive
        self.scarab = None

    def activate(self):
        self.state = State.active

    def deactivate(self):
        self.state = State.inactive

    def pause(self):
        self.state = State.paused

    def resume(self):
        self.state = State.active

    def abort(self):
        self.state = State.aborted

    def freeze(self):
        self.state = State.frozen

    def defreeze(self):
        self.state = State.inactive

