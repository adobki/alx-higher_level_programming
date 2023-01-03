#!/usr/bin/python3
"""This is a Rectangle class module with some extra code for testing."""


class Rectangle():
    """A Rectangle with width and height attributes/fields."""

    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Placeholder doc string."""

        try:
            if not isinstance(rect_1, Rectangle):
                raise TypeError('rect_1 must be an instance of Rectangle')
            elif not isinstance(rect_2, Rectangle):
                raise TypeError('rect_2 must be an instance of Rectangle')
            # else:
            #     print('     __       __     {}'.format(str(rect_1.area)))
            #     print('     __       __     {}'.format(rect_2.area))
            # elif rect_2.area > rect_1.area:
            #     return rect_2
            else:
                return rect_1
        except Exception as err:
            print(err)

    def __init__(self, width=0, height=0):
        """
        Initialises a new instance of Rectangle and sets its size.

        :param width: Width of the Rectangle.
        :param height: Height of the Rectangle.
        """
        self.__width = width
        self.__height = height

    def __del__(self):
        """Action(s) to perform when an instance of the class is deleted."""
        print('Bye rectangle...')

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

    def area(self):
        """
        Returns the area of the current Rectangle.

        :return: Area of Rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the current Rectangle.

        :return: perimeter of Rectangle (2 * (width + height)).
        """
        return 2 * (self.__width + self.__height)

    def print(self):
        """Prints the Rectangle with the character #."""
        if self.__width == 0:
            print()
        else:
            for num1 in range(self.__height):
                for num2 in range(self.__width):
                    print(self.print_symbol, end='')
                if num1 is not self.__height - 1:
                    print()

    # def __repr__(self):
    #     """Handle the __repr__ class method."""
        # return '        Nothing to print. . .yet! ;-)'

    def __str__(self):
        """
        Rectangle printer property.

        Calls the print method when instance is passed to print().
        """
        self.print()
        return ''


def main():
    """Tests the code."""

    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")


if __name__ == "__main__":
    main()
