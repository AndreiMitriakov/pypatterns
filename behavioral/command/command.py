#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod, ABCMeta


# Receiver
class Bulb:

    def __init__(self):
        pass

    def turn_on(self):
        print('Bulb is on')

    def turn_off(self):
        print('Bulb is off')


#Command
class Command(ABC):
    
    def execute(self):
        pass
    
    def undo(self):
        pass

    def redo(self):
        pass


class TurnOn(Command):

    def __init__(self, bulb):
        self.bulb = bulb

    def execute(self):
        self.bulb.turn_on()


    def undo(self):
        self.bulb.turn_off()

    def redo(self):
        self.execute()

class TurnOff(Command):

    def __init__(self, bulb):
        self.bulb = bulb

    def execute(self):
        self.bulb.turn_off()

    def undo(self):
        self.bulb.turn_on()

    def redo(self):
        self.execute()

#Invoker
class RemoteControl:

    def submit(self, command):
        command.execute()

if __name__ == '__main__':
    bulb = Bulb()
    turn_on = TurnOn(bulb)
    turn_off = TurnOff(bulb)
    remote = RemoteControl()
    remote.submit(turn_on)
    remote.submit(turn_off)

