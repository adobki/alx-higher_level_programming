#!/usr/bin/python3
"""This is a Square class module with some extra code for testing."""


class Square():
    """A Square with size and position attributes/fields."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises a new instance of Square and sets its size.

        :param size: Size of the Square.
        :param position: Coordinates of square when printed on screen.

        :return: Number of elements printed.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Retrieves private instance attribute __size.

        :return: Size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Data validator for given size attribute.

        :param size: Size of Square passed to class object by user.
        """
        try:
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        except Exception as err:
            print(err)
            del self

    @property
    def position(self):
        """
        Retrieves private instance attribute __position.

        :return: position of square when printed on screen.
        """
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        """
        Data validator for given position attribute.

        :param position: Coordinates of square when printed on screen.
        """
        try:
            if not isinstance(position, tuple):
                raise TypeError
            elif position[0] < 0 or position[1] < 0:
                raise TypeError
            else:
                self.__position = position
        except Exception as err:
            print('position must be a tuple of 2 positive integers')
            del self

    def area(self):
        """
        Returns the area of the current Square.

        :return: Area of Square (size^2).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] >= 1:
                print(' ' * (self.__position[1] * self.__position[1]))
            for num1 in range(self.__size):
                if self.__position[1] == 0:
                    for num2 in range(self.__position[0]):
                        print(' ', end='')
                for num2 in range(self.__size):
                    print('#', end='')
                print()

    def __repr__(self):
        """Handle the __str__ class method for the singly-linked list."""
        return '        Nothing to print. . .yet! ;-)'

    def __str__(self):
        """
        Square printer property.

        Calls the my_print method when instance is passed to print().
        """
        self.my_print()
        return ''


def main():
    """Tests the code."""

    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)


if __name__ == "__main__":
    main()
