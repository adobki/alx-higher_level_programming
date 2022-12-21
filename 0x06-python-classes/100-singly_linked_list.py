#!/usr/bin/python3
"""
This is a singly-linked list module (SLL for short).

It defines two classes, with some extra code for testing them:
    1. SinglyLinkedList
    2. Node
"""


class SinglyLinkedList():
    """A singly-linked list with automatic sorting of data."""

    def __init__(self):
        """Initialises a new instance of SLL and sets its data."""

        self.__node = []
        # self.__data = data

    def __repr__(self):
        """Handle the __str__ class method for the singly-linked list."""
        return '        Nothing to print. . .yet! ;-)'

    def __str__(self):
        """
        Singly-linked list printer.

        Prints the contents of the one line at a time list when \
        an instance of the SSL is passed to print function.
        """
        print_str = ''
        for data in sorted(self.__node, reverse=True):
            print_str = '{}\n'.format(data) + print_str
        return print_str

    def head(self):
        """
        Returns the area of the current Square.

        :return: Area of Square (size^2).
        """
        # return self.__data
        return ['self.__data']

    def sorted_insert(self, data=None):
        """Prints the square with the character #."""
        try:
            if not data or not isinstance(data, int):
                raise TypeError('data must be an integer')
            else:
                self.__node.append(data)
        except Exception as err:
            print(err)
            del self


# class Node(SinglyLinkedList):
class Node():
    """A singly-linked list (SLL) head node."""

    def __init__(self, data, next_node=None):
        """Initialises a new instance of SLL and sets its data."""

        # SinglyLinkedList.__init__()
        self.__data = data
        self.__next_node = next_node

        @property
        def data(self):
            """Retrieves private instance attribute __data."""
            return self.__data

        @data.setter
        def data(self, data=0):
            """Assigns data to private instance attribute __position."""
            self.__data = data

        @property
        def next_node(self):
            """Retrieves private instance attribute __next_node."""
            return self.__data

        @data.setter
        def next_node(self, next_node=None):
            """Assigns data to private instance attribute __next_node."""
            self.__next_node = next_node


def main():
    """Tests the code."""

    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)

    sll.sorted_insert()

    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)


if __name__ == "__main__":
    main()
