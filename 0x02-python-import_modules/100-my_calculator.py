#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a, b, operator = int(argv[1]), int(argv[3]), argv[2]
    if operator == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif operator == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif operator == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif operator == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
