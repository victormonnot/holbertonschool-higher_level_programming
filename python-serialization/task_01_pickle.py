#!/usr/bin/python3
"""file"""


import pickle


class CustomObject:
    """Class with serialization"""

    def __init__(self, name, age, is_student):
        """Initialize"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
