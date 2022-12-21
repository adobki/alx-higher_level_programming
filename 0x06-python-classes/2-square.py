#!/usr/bin/python3
"""This is a Square class module with some extra code for testing."""


class Square():
    """A Square with a size attribute/field."""

    def __init__(self, size=0):
        """
        Initialises a new instance of Square and sets its size.

        :param size: Size of the Square.
        """
        self.__size = size
        try:
            if type(size) != type(0):
                raise TypeError
            if self.__size < 0:
                raise ValueError
        except (TypeError) as err:
            print('size must be an integer')
            del self
        except ValueError as err:
            print('size must be >= 0')
            del self
        else:
            self.__size = int(size)


def main():
    """Tests the code."""

    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)

    # print(type('12df') == type(None), end='\n[Joker!]\n')
    # try:
    #     print(int('12df'), end='\n[Joker!]\n')
    # except Exception as err:
    #     print('size must be an integer')


if __name__ == "__main__":
    main()
