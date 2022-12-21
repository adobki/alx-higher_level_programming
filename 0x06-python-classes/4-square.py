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
        Returns the area of the Square.

        :return: Area of Square (size^2).
        """
        return self.__size ** 2


def main():
    """Tests the code."""

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

    # print(int('12df'), end='\n[Joker!]\n')
    # try:
    #     print(int('12df'), end='\n[Joker!]\n')
    # except Exception as err:
    #     print('size must be an integer')


if __name__ == "__main__":
    main()
