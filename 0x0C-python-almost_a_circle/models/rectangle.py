#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    Class representing a rectangle, derived from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): X-coordinate of the top-left corner of the rectangle.
        - y (int): Y-coordinate of the top-left corner of the rectangle.
        - id (int): Optional. If provided, sets the id of the instance;

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        int: Width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
        - value (int): Width value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
        int: Height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
        - value (int): Height value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the top-left corner of the rectangle.

        Returns:
        int: X-coordinate of the rectangle.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the top-left corner of the rectangle.

        Parameters:
        - value (int): X-coordinate value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the top-left corner of the rectangle.

        Returns:
        int: Y-coordinate of the rectangle.

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the top-left corner of the rectangle.

        Parameters:
        - value (int): Y-coordinate value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        int: Area of the rectangle.

        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle by printing '#' characters.

        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        str: String representation of the rectangle.

        """
        a = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        return a + f"- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Parameters:
        - args (tuple): Positional arguments.
        - kwargs (dict): Keyword arguments.

        """
        # Implementation...

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle.

        Returns:
        dict: Dictionary representation of the rectangle.

        """
        return {
            'x': self.__x,
            'width': self.__width,
            'id': self.id,
            'height': self.__height,
            'y': self.__y
        }
