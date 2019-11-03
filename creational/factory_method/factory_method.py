from abc import ABC, abstractmethod

class Product:

    def __init__(self):
        self.value = None

    @property
    @abstractmethod
    def type(self):
        pass

    @type.setter
    @abstractmethod
    def type(self, value):
        pass

class ProductA(Product):

    def __init__(self):
        self.value = None

    @property
    @abstractmethod
    def type(self):
        return self.type_

    @type.setter
    @abstractmethod
    def type(self, value):
        self.type_ = value

class ProductB(Product):

    def __init__(self):
        self.value = None

    @property
    @abstractmethod
    def type(self):
        return self.type_

    @type.setter
    @abstractmethod
    def type(self, value):
        self.type_ = value

class Creator(ABC):
    @abstractmethod
    def make_product(self):
        pass

class ConcreteCreatorA(Creator):
    
    def make_product(self):
        return ProductA()

class ConcreteCreatorB(Creator):
    
    def make_product(self):
        return ProductB()

if __name__ == '__main__':
    cA = ConcreteCreatorA()
    pA = cA.make_product()
    pA.type = 'A'
    cB = ConcreteCreatorB()
    pB = cB.make_product()
    pB.type = 'B'
    print('Products {}, {}'.format(pA.type, pB.type))
