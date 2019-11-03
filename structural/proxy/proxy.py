#!/usr/bin/env python3
# coding: utf-8


'''
Proxy is a wrapper giving access to another class.
It can forward queries to another class or even add some new logic.
'''

class Door:

    def open(self):
        print('Opening')

    def close(self):
        print('Closing')

class Security:

    def __init__(self, door: Door):
        self.door = door
        
    def open(self, password):
        if(self.authentificate(password)):
            self.door.open()
        else:
            print('Access denied')

    def authentificate(self, password):
        return password == '1234'

    def close(self):
        self.door.close()

if __name__ == '__main__':

    door = Security(Door())
    door.open('4321')
    door.open('1234')
    
