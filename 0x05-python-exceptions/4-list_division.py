#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element across two lists.

    :param my_list_1: List with numerators.
    :param my_list_2: List with denominators.
    :param list_length: Number of elements to be divided.

    :return: List with results of divisions
    """
    if my_list_1 is not None and my_list_2 is not None and list_length > 0:
        my_list_results = []
        for index in range(list_length):
            result = 0
            try:
                a, b = my_list_1[index], my_list_2[index]
                result = a / b
            except IndexError:
                print('out of range')
            except TypeError:
                print('wrong type')
            except ZeroDivisionError:
                print('division by 0')
            finally:
                my_list_results.append(result)
        return my_list_results
    return []


def main():
    """Tests the code."""
    lst_x, lst_y, val_z = (10, 8, 4), (2, 4, 4), 3
    print('{}'.format(list_division(lst_x, lst_y, val_z)))

    print("    -  -")

    lst_x, lst_y, val_z = (10, 8, 4, 4), (2, 0, 'H', 2, 7), 5
    print('{}'.format(list_division(lst_x, lst_y, val_z)))

    print("    -  -")
    print('{}'.format(list_division([], (), 0)))


if __name__ == "__main__":
    main()
