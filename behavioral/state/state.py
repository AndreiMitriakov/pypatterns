#!/usr/bin/env python3
# coding: utf-8
from abc import ABC, abstractmethod
class WritingState(ABC):

    @abstractmethod
    def write(self, words: str):
        pass

class UpperCase(WritingState):

    def write(self, words: str):
        print(words.upper())

class LowerCase(WritingState):

    def write(self, words: str):
        print(words.lower())

class Default(WritingState):

    def write(self, words: str):
        print(words)

class TextEditor:

    def __init__(self, state: WritingState):
        self.state_ = state

    def set_state(self, state: WritingState):
        self.state_ = state

    def type(self, words: str):
        self.state_.write(words)

if __name__ == '__main__':
    editor = TextEditor(Default())
    editor.type('First')
    editor.set_state(UpperCase())
    editor.type('Second')
    editor.set_state(LowerCase())
    editor.type('Third')

