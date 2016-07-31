#!/usr/bin/python3


from enum import Enum


STATE_ERROR = "Incorrect task state"


class State(Enum):
    inactive = 1
    active = 2
    running = 3
    paused = 4
    aborted = 5
    completed = 6
    failed = 7
    frozen = 8


class Task(object):
 
    def __init__(self, name, scarab_name):
        self.state = State.inactive
        self.__scarab_name = scarab_name
        self.name = name
        self.scheduler = None

    def activate(self):
        assert self.state == State.inactive, STATE_ERROR
        self.state = State.active

    def deactivate(self):
        assert self.state in [State.active, State.completed], STATE_ERROR
        self.state = State.inactive

    def run(self):
        assert self.state in [State.active, State.completed], STATE_ERROR
        self.state = State.running
        self.scheduler.overseer.run_scarab(self.__scarab_name)

    def pause(self):
        assert self.state == State.running, STATE_ERROR
        self.state = State.paused

    def resume(self):
        assert self.state == State.paused, STATE_ERROR
        self.state = State.active

    def abort(self):
        assert self.state == State.running, STATE_ERROR
        self.state = State.aborted

    def freeze(self):
        assert self.state == State.inactive, STATE_ERROR
        self.state = State.frozen

    def defreeze(self):
        assert self.state == State.frozen, STATE_ERROR
        self.state = State.inactive

