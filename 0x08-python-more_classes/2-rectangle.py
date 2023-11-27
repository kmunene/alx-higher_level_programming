#!/usr/bin/python3
class Rectangle:
    """
    Rectangle Class

    This class represents a rectangle with width and height attributes.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Author: kelvin munene
    Date: 11/27/2023

    """

    def __init__(self, width=0, height=0):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.

        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        A = self.__height * self.__width
        return A

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            P = (self.__width * 2) + (self.__height * 2)
            return P
