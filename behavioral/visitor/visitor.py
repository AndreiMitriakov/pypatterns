#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod, ABCMeta


class Animal(ABC):

    @abstractmethod
    def accept(self, operation):
        pass        


class AnimalOperation(ABC):

    @abstractmethod
    def visit_monkey(self, monkey):
        pass

    @abstractmethod
    def visit_lion(self, lion):
        pass

    @abstractmethod
    def visit_dolphin(self, dolphin):
        pass
        

class Monkey(Animal):

    def shout(self):
        print('Ooh oo aa aa!')

    def accept(self, operation):
        operation.visit_monkey(self)

class Lion(Animal):

    def shout(self):
        print('Roaaar!')

    def accept(self, operation):
        operation.visit_lion(self)

class Dolphin(Animal):

    def shout(self):
        print('Tuut tuttu tuutt!')

    def accept(self, operation):
        operation.visit_dolphin(self)

class Speak(AnimalOperation):

    def visit_monkey(self, monkey):
        monkey.shout()

    def visit_lion(self, lion):
        lion.shout()

    def visit_dolphin(self, dolphin):
        dolphin.shout()

if __name__ == '__main__':
    monkey = Monkey()
    lion = Lion()
    dolphin = Dolphin()

    speak = Speak()

    monkey.accept(speak)
    lion.accept(speak)
    dolphin.accept(speak)

