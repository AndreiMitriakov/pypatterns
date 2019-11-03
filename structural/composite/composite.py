#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod

'''
Composite allows to manipulate with a group of objects like with one. 
'''

class Employee(ABC):
    @abstractmethod
    def __init__(self, name, salary):
        pass

    @abstractmethod    
    def  get_name(self):
        pass

    @abstractmethod    
    def  get_salary(self):
        pass

    @abstractmethod    
    def  get_name(self):
        pass

    @abstractmethod    
    def  get_salary(self):
        pass

    @abstractmethod    
    def  get_roles(self):
        pass

class Dev(Employee):
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def get_roles(self):
        return self.roles

    def set_salary(self, value):
        self.salary = value

class Designer(Employee):
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def get_roles(self):
        return self.roles

    def set_salary(self, value):
        self.salary = value

class Organization:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_salary(self):
        salary = 0.
        for employee in self.employees:
            salary += employee.get_salary()
        return salary

if __name__ == '__main__':
    jt = Dev('JT', 1000)
    jb = Dev('JB', 900)
    jc = Dev('JC', 1100)
    jp = Dev('JP', 400)

    organization1 = Organization()
    organization1.add_employee(jt)
    organization1.add_employee(jb)

    organization2 = Organization()
    organization2.add_employee(jc)
    organization2.add_employee(jp)  
    organization2.add_employee(organization1)

    print('Organization 1 salary {}'.format(organization1.get_salary()))
    print('Organization 2 salary {}'.format(organization2.get_salary()))

