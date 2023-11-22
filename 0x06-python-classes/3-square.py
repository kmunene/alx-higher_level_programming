#!/usr/bin/python3


# Author: kelvin


class Square:
    '''innitialize the class'''
    def __init__(self, size=0):
        self.__size = size
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        '''returns area'''
        s = self.__size * self.__size
        return s
