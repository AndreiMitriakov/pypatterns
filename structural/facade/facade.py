#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod

'''
Facade proposes a simple interface for a complex system.
'''


class Computer:

    def power_suply(self):
        print('Power suply')

    def post(self):
        print('Power-on self-test')

    def show_loading_screen(self):
        print('Loading screen')

    def BIOS(self):
        print('Accessing the first sector')

    def BIOS_confirmation(self):
        print('BIOS confirms there\'s a bootstrap loader')

    def loading_os(self):
        print('Loading operating system into memory')

    def turn_control(self):
        print('Control is passed over OS')

class ComputerUserFacade:

    def __init__(self, pc: Computer):
        self.pc = pc

    def turn_on(self):
        self.pc.power_suply()
        self.pc.post()
        self.pc.show_loading_screen()
        self.pc.BIOS()
        self.pc.BIOS_confirmation()
        self.pc.loading_os()
        self.pc.turn_control()

if __name__ == '__main__':
    pc = Computer()
    ui = ComputerUserFacade(pc)
    ui.turn_on()
