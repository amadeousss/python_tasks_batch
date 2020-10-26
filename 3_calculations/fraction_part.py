# -*- coding: utf-8 -*-

"""
This program prints fractional part of given number.
"""


try:
    number = list(input())
except ValueError:
    print('Incorrect input')

print("".join(number[number.index('.')+1:]))

