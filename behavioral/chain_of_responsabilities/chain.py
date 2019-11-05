#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod, ABCMeta

class Account:

    def __init__(self):
        self.successor = None
        self.balance = None

    def set_next(self, account):
        self.successor = account

    def pay(self, amount: float):
        if self.can_pay(amount):
            print('Paid {} using {}'.format(amount, self.__class__.__name__))
        elif self.successor:
            print('Can not pay using {}'.format(self.__class__.__name__))
            self.successor.pay(amount)
        else:
            raise Exception('No money')

    def can_pay(self, amount):
        return self.balance >= amount

class Bank(Account):

    def __init__(self, balance):
        self.balance = balance

class Paypal(Account):

    def __init__(self, balance):
        self.balance = balance

class Bitcoin(Account):

    def __init__(self, balance):
        self.balance = balance

if __name__ == '__main__':        
    bank = Bank(100)
    paypal = Paypal(200)
    bitcoin = Bitcoin(300)
    bank.set_next(paypal)
    paypal.set_next(bitcoin)
    bank.pay(250)

