#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod

'''
Adapter is used to work with a not compatible class creating a wrapper over it.
'''

class Lion(ABC):
    @abstractmethod
    def roar(self) -> str:
        pass

class AsianLion(Lion):
    def roar(self) -> str:
        return 'roar'

class AfricanLion(Lion):
    def roar(self) -> str:
        return 'roar'

class WildDog:
    def bark(self) -> str:
        return 'bark'

class WildDogAdapter(Lion):
    def __init__(self, dog: WildDog) -> None:
        self.dog = dog

    def roar(self):
        return self.dog.bark()

class Hunter:
    def hunt(self, lion: Lion) -> None:
        
        noise = lion.roar()
        if noise:
            print('Hunting')

if __name__ == '__main__':
    wild_dog = WildDog()
    wild_dog_adapter = WildDogAdapter(wild_dog)
    hunter = Hunter()
    hunter.hunt(wild_dog_adapter)
    try:
        hunter.hunt(wild_dog)
    except:
        print('Can not hunt')
