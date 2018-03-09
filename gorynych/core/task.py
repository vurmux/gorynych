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

    def __init__(self, name, scarab, scarab_config):
        self._state = State.inactive
        self._scarab = scarab
        self._scarab_config = scarab_config
        self.name = name
        self.priority = 0

    @property
    def scarab(self):
        return self._scarab

    @property
    def scarab_config(self):
        return self._scarab_config

    @property
    def state(self):
        return self._state

    def activate(self):
        assert self._state == State.inactive, STATE_ERROR
        self._state = State.active

    def deactivate(self):
        assert self._state in [State.active, State.completed], STATE_ERROR
        self._state = State.inactive

    def run(self):
        assert self._state in [State.active, State.completed], STATE_ERROR
        self._state = State.running
        self._scarab.run(self._scarab_config)

    def pause(self):
        assert self._state == State.running, STATE_ERROR
        self._state = State.paused

    def resume(self):
        assert self._state == State.paused, STATE_ERROR
        self._state = State.active

    def abort(self):
        assert self._state == State.running, STATE_ERROR
        self._state = State.aborted

    def freeze(self):
        assert self._state == State.inactive, STATE_ERROR
        self._state = State.frozen

    def defreeze(self):
        assert self._state == State.frozen, STATE_ERROR
        self._state = State.inactive
