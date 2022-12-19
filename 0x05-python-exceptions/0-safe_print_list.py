#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    :param my_list: List to be printed.
    :param x: Number of elements in my_list to be printed.

    :return: Number of elements printed.
    """
    countr = 0
    if my_list is not None and x > 0:
        for item in range(x):
            try:
                print("{}".format(my_list[item]), end='')
            except IndexError:
                print()
                return countr
            else:
                countr += 1
    print()
    return countr


def main():
    """Tests the code."""

    # my_list = [1, 2, 3, 4, 5]
    my_list = [1, '2', 3, '4', 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, 5)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, 5 + 2)
    print("nb_print: {:d}".format(nb_print))


if __name__ == "__main__":
    main()
