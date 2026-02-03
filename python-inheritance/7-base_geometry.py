#!/usr/bin/python3
'''base_geometry'''


class BaseGeometry:
    '''Base Geometry Class'''

    def area(self):
        '''raise Exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validate Integer'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
