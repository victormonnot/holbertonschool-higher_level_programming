#!/usr/bin/python3
'''square'''


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    '''Square class that inherite from Rectangle'''

    def __init__(self, size):
        '''.'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        