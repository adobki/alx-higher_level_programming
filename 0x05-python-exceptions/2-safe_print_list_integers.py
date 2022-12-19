#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints x elements of a list if each one is an integer.

    :param my_list: List to be printed.
    :param x: Number of elements in my_list to be printed.

    :return: Number of elements printed.
    """
    countr = 0
    if my_list is not None and x > 0:
        for item in range(x):
            try:
                print("{:d}".format(my_list[item]), end='')
            except IndexError:
                raise
            except Exception:
                pass
            else:
                countr += 1
    print()
    return countr


def main():
    """Tests the code."""

    # my_list = [1, '2', 3, '4', 5]
    # print('printed: {}'.format(safe_print_list_integers(my_list, 7)))

    # Example from project: #
    print()
    # my_list = [1, 2, 3, 4, 5]
    #
    # nb_print = safe_print_list_integers(my_list, 7)
    # print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, 6)
    print("nb_print: {:d}".format(nb_print), end='\n\n')

    nb_print = safe_print_list_integers(my_list, 6 + 20)
    print("nb_print: {:d}".format(nb_print))


if __name__ == "__main__":
    main()
