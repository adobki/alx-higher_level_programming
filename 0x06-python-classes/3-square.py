#!/usr/bin/python3
"""This is a Square class module with some extra code for testing."""


class Square():
    """A Square with a size attribute/field."""

    def __init__(self, size=0):
        """
        Initialises a new instance of Square and sets its size.

        :param size: Size of the Square.
        """
        try:
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        except TypeError as err:
            print(err)
            self.__size = 0
        except ValueError as err:
            print(err)
            self.__size = 0

    def area(self):
        """
        Returns the area of the Square.

        :return: Area of Square (size^2).
        """
        return self.__size ** 2


def main():
    """Tests the code."""

    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))

    # print(type('12df') == type(None), end='\n[Joker!]\n')
    # try:
    #     print(int('12df'), end='\n[Joker!]\n')
    # except Exception as err:
    #     print('size must be an integer')


if __name__ == "__main__":
    main()
