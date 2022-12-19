#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result.

    :param a: Numerator.
    :param a: Denominator.

    :return: Value of division on success.
             None on error.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print('Inside result: {}'.format(result))
        return result


def main():
    """Tests the code."""
    a, b = 12, 2
    print('{} / {} = {}'.format(a, b, safe_print_division(a, b)))

    a, b = 12, 0
    print('{} / {} = {}'.format(a, b, safe_print_division(a, b)))


if __name__ == "__main__":
    main()
