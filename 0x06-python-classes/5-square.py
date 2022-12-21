#!/usr/bin/python3
"""This is a Square class module with some extra code for testing."""


class Square():
    """A Square with a size attribute/field."""

    def __init__(self, size=0):
        """
        Initialises a new instance of Square and sets its size.

        :param size: Size of the Square.

        :return: Number of elements printed.
        """
        self.__size = size

    @property
    def size(self):
        """
        Assigns argument size to private instance attribute __size.

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
            for num1 in range(self.__size):
                for num2 in range(self.__size):
                    print('#', end='')
                print()


def main():
    """Tests the code."""

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

    # print(int('12df'), end='\n[Joker!]\n')
    # try:
    #     print(int('12df'), end='\n[Joker!]\n')
    # except Exception as err:
    #     print('size must be an integer')


if __name__ == "__main__":
    main()
