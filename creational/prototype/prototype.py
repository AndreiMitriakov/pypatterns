from datetime import datetime
from copy import deepcopy
from typing import Any
from abc import ABCMeta, abstractproperty

class Sheep:

    def __init__(self):
        self._name = None
        self._circular_reference = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_):
        self._name = name_

    @property
    def circular_reference(self):
        return self._circular_reference

    @circular_reference.setter
    def circular_reference(self, value):
        self._circular_reference = value

    def clone(self):
        return deepcopy(self)

class ComponentWithBackReference:
    def __init__(self, prototype):
        self._prototype = prototype

    @property
    def prototype(self):
        return self._prototype

    @prototype.setter
    def prototype(self, value):
        self._prototype = value

if __name__ == '__main__':
    dolly = Sheep()
    dolly.name = 'Dolly'
    dolly.circular_reference = ComponentWithBackReference(dolly)
    print(id(dolly.name), dolly.name)
    barry = dolly.clone()
    barry.name = 'Barry'
    print(id(barry.name), barry.name)

