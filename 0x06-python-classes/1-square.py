#!/usr/bin/python3
""" definition of class Square"""

class Square:
    """Represents a square
    Attributes:
        __size (int) : size of a side of square
    """
    def __init__(self, size):
        """Initializes a suare
        Args:
            size (int): size of a side of square
        Returns: None
        """
        self.__size = size
