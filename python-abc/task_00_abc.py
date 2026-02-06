#!/usr/bin/env python3
'''file'''


from abc import ABC, abstractmethod
class Animal(ABC):
    '''Class'''

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
