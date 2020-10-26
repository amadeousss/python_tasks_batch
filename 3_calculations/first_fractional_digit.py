# -*- coding: utf-8 -*-

"""
This program print first digit of fractional part
of a given number.
"""

try:
    number = float(input())
except ValueError:
    print('Incorrect input')

print(int(number*10)%10)

