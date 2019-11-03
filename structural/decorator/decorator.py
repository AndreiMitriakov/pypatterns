#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod

'''
Wraps a class with new functionalities.
'''

class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class SimpleCoffee(Coffee):

    def get_cost(self):
        return 5

    def get_description(self):
        return 'Simple coffee'

class MilkCoffee(Coffee):
    
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 3

    def get_description(self):
        return self.coffee.get_description() + ', milk'

if __name__ == '__main__':
    coffee = SimpleCoffee()
    print(coffee.get_description())
    milk_coffee = MilkCoffee(coffee)
    print(milk_coffee.get_description())
    
