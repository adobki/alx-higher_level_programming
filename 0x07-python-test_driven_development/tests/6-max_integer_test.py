#!/usr/bin/python3
"""Module runs unittests for the max_integer function."""

import unittest
# from max_integer import max_integer
max_integer = __import__('6-max_integer').max_integer

print(max_integer())
print()
print(max_integer([4, 9, 3, 12, 0]))
print()
print(max_integer(['3', '4']))
print()
print(max_integer('Three'))
print()
