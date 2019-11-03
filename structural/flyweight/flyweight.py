#!/usr/bin/env python3
# coding: utf-8

'''
Flyweight allows for objects to use sharing memory in order to decreace memory consumption.
'''

class Tea:
    pass

class BlackTea(Tea):
    pass

class GreenTea(Tea):
    pass

class TeaMaker:

    def __init__(self):
        self.tea = {}
        self.possible_teas = {'green': GreenTea, 'black': BlackTea}

    def make(self, pref):
        if pref not in self.tea.keys():
            self.tea[pref] = self.possible_teas[pref]()
        return id(self.tea[pref])

class TeaShop:
    
    def __init__(self, tea_maker):
        self.orders = {}
        self.tea_maker = tea_maker
        
    def take_order(self, pref: str, table: int) -> None:
        self.orders[table] = self.tea_maker.make(pref)
        return self.orders[table]

if __name__ == '__main__':

    tea_maker = TeaMaker()
    shop = TeaShop(tea_maker)
    print('Tea from the container {} '.format(shop.take_order('green', 1)))
    print('Tea from the container {} '.format(shop.take_order('green', 2)))
    print('Tea from the container {} '.format(shop.take_order('black', 3)))
    print('Tea from the container {} '.format(shop.take_order('black', 4)))
