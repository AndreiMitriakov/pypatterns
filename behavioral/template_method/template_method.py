#!/usr/bin/env python3
# coding: utf-8
from abc import ABC, abstractmethod
class Builder(ABC):

    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def lint(self):
        pass

    @abstractmethod
    def assemble(self):
        pass

    @abstractmethod
    def deploy(self):
        pass

class AndroidBuilder(Builder):

    def test(self):
        print("Running android tests")

    def lint(self):
        print("Linting the android code")

    def assemble(self):
        print("Assembling the android build")

    def deploy(self):
        print("Deploying android build to server")

class IOSBuilder(Builder):

    def test(self):
        print("Running ios tests")

    def lint(self):
        print("Linting the ios code")

    def assemble(self):
        print("Assembling the ios build")

    def deploy(self):
        print("Deploying ios build to server")

if __name__ == '__main__':
    android_builder = AndroidBuilder()
    android_builder.build()
    ios_builder = IOSBuilder()
    ios_builder.build()

