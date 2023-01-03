#!/usr/bin/python3
"""This is a Rectangle class module with some extra code for testing."""


class Rectangle():
    """A Rectangle with width and height attributes/fields."""

    def __init__(self, width=0, height=0):
        """
        Initialises a new instance of Rectangle and sets its size.

        :param width: Width of the Rectangle.
        :param height: Height of the Rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Assigns argument width to private instance attribute __width.

        :return: Width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Data validator for given width attribute.

        :param width: Width of Rectangle passed to class object by user.
        """
        try:
            if not isinstance(width, int):
                raise TypeError('width must be an integer')
            elif width < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = width
        except Exception as err:
            print(err)
            del self

    @property
    def height(self):
        """
        Assigns argument height to private instance attribute __height.

        :return: Height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Data validator for given height attribute.

        :param height: Height of Rectangle passed to class object by user.
        """
        try:
            if not isinstance(height, int):
                raise TypeError('height must be an integer')
            elif height < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = height
        except Exception as err:
            print(err)
            del self


def main():
    """Tests the code."""

    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)


if __name__ == "__main__":
    main()
