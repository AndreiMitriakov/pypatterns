#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod

'''
Bridge allows to distinguish abstraction and implementation.
'''

class Theme(ABC):
    
    def get_color(self) -> str:
        pass

class Page(ABC):

    @abstractmethod
    def __init__(self, theme: Theme) -> None:
        pass

    @abstractmethod
    def get_content(self):
        pass

class About(Page):
    
    def __init__(self, theme: Theme) -> None:
        self.theme = theme

    def get_content(self) ->str:
        return 'About page in {}'.format(self.theme.get_color())

class Careers(Page):
    
    def __init__(self, theme: Theme) -> None:
        self.theme = theme

    def get_content(self) ->str:
        return 'Career page in {}'.format(self.theme.get_color())

class DarkTheme(Theme):
    
    def get_color(self) -> str:
        return 'dark'

class LightTheme(Theme):
    
    def get_color(self) -> str:
        return 'light'

if __name__ == '__main__':
    about = About(DarkTheme())
    careers = Careers(LightTheme())
    print(about.get_content())
    print(careers.get_content())
