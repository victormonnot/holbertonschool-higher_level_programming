#!/usr/bin/python3
'''file'''


class Student:
    '''Class to create a Student'''

    def __init__(self, first_name, last_name, age):
        '''To create a class'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''to JSON'''
        return self.__dict__
