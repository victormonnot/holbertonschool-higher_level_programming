#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Square with size, area and print"""

    def __init__(self, size=0):
        """Initializes the class with size"""
        self.size = size

    @property
    def size(self):
        """Getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(self.__size * "#")
