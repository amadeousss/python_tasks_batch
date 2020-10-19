# -*- coding: utf-8 -*-

"""
This program prints fractional part of given number
"""


try:
    number = list(input())
    print("".join(number[number.index('.')+1:]))
except ValueError:
    print('Incorrect input')
