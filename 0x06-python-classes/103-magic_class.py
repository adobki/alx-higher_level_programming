#!/usr/bin/python3
"""This is a Square class module with some extra code for testing."""


class MagicClass():
    """A Square with size and position attributes/fields."""

    def __init__(self, radius=0):
        """
        Initialises a new instance of Square and sets its size.

        :param radius: Size of the Square.
        """
        self.__radius = radius
        self.__area = self.__circumference = 0

    @property
    def radius(self):
        """Getter for __radius field via radius property."""
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """
        Data validator for given radius attribute.

        :param radius: Radius passed to class instance by user.
        """
        try:
            if not isinstance(radius, int):
                raise TypeError('radius must be a number')
            elif radius < 0:
                raise ValueError('radius must be >= 1')
            else:
                self.__radius = radius
        except Exception as err:
            print(err)
            del self

    @property
    def area(self):
        """Getter for __area field via area property."""
        return self.__area

    @area.setter
    def area(self, area):
        """
        Data validator for given area attribute.

        :param area: Area passed to class instance by user.
        """
        self.__area = area

    @property
    def circumference(self):
        """Getter for __circumference field via circumference property."""
        return self.__circumference

    @circumference.setter
    def circumference(self, circumference):
        """
        Data validator for given circumference attribute.

        :param circumference: Circumference passed to class instance by user.
        """
        self.__circumference = circumference


def main():
    """Tests the code."""

    my_square = MagicClass(55)
    print(my_square)

    print("--")

    my_square = MagicClass(55)
    print(my_square)

    my_square.radius = 33
    my_square.area = 51
    my_square.circumference = 50
    print([my_square.area, my_square.radius, my_square.circumference])


if __name__ == "__main__":
    main()
