#!/usr/bin/env python3

from abc import ABC, ABCMeta, abstractmethod, abstractproperty
from typing import Any

class Director:
    def __init__(self, builder):
        self.builder = builder

    def change_builder(self, builder):
        self.builder = builder

    def make(self, product_type):
        self.builder.reset()
        if product_type == 'A':
            self.builder.produce_part_1()
        elif product_type == 'B':
            self.builder.produce_part_2()
            self.builder.produce_part_3()
            

class Builder:
    @abstractmethod
    def produce_part_1(self) -> None:
        pass

    @abstractmethod
    def produce_part_2(self) -> None:
        pass

    @abstractmethod
    def produce_part_3(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    
    def __init__(self):
        self.reset()

    def product(self):
        """I'm the 'x' property."""
        return self.product

    def reset(self):
        self.product = Product()

    def produce_part_1(self):
        self.product.add('Diesel engine')

    def produce_part_2(self):
        self.product.add('Bensin engine')

    def produce_part_3(self):
        self.product.add('Documentation')


class Product:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")
        print('\n')



def client():
    print('inside')
    b = ConcreteBuilder1()
    d = Director(b)
    type_ = 'B'
    d.make(type_)
    product = b.product
    product.list_parts()
    

if __name__ == '__main__':
    client()
