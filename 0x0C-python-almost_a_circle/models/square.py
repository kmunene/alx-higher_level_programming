#!/usr/bin/python3

from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    Class representing a square, derived from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): Size of the square.
        - x (int): X-coordinate of the top-left corner of the square.
        - y (int): Y-coordinate of the top-left corner of the square.
        - id (int): Optional. If provided, sets the id of the instance;

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: String representation of the square.

        """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
        int: Size of the square.

        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        - value (int): Size value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Parameters:
        - args (tuple): Positional arguments.
        - kwargs (dict): Keyword arguments.

        """
        # Implementation...

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
        dict: Dictionary representation of the square.

        """
        return {
            'id': self.id,
            'x': self.__x,
            'size': self.size,
            'y': self.__y
        }
