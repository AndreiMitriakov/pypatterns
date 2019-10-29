#!/usr/bin/env python3
# coding: utf-8
from abc import ABC, abstractmethod, ABCMeta

class AbsctractTable(ABC):

    @abstractmethod
    def table_view(self):
        pass

class AbsctractChair(ABC):

    @abstractmethod
    def chair_view(self):
        pass

class ModernChair(AbsctractChair):
    def chair_view(self):
        return 'modern_chair'

class ModernTable(AbsctractTable):
    def table_view(self):
        return 'modern_table'

class OldChair(AbsctractChair):
    def chair_view(self):
        return 'old_chair'

class OldTable(AbsctractTable):
    def table_view(self):
        return 'old_table'

class AbstractFactory(ABC):

    chairs = 0
    tables = 0    

    def inc_tables(cls):
        cls.tables += 1

    def inc_chairs(cls):
        cls.chairs += 1

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self, output, data):
        pass

class ModernFactory(AbstractFactory):

    def create_chair(self):
        self.inc_chairs()
        return ModernChair()

    def create_table(self):
        self.inc_tables()
        return ModernTable()

class OldFactory(AbstractFactory):

    def create_chair(self):
        self.inc_chairs()        
        return OldChair()

    def create_table(self):
        self.inc_tables()
        return OldTable()

if __name__ == '__main__':
    old_factory = OldFactory()
    modern_factory = ModernFactory()
    print('Num chairs: {}'.format(old_factory.chairs))
    print('Old chair creation')
    chair = old_factory.create_chair()
    print('Num chairs: {}'.format(old_factory.chairs))
    print('Chair view: {}'.format(chair.chair_view()))



