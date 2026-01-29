#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Square with getter, setter, and area"""

    def __init__(self, size=0):
        """Initialize square with size"""
        self.size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return area of square"""
        return self.__size * self.__size
