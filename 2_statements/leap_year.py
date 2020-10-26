# -*- coding: utf-8 -*-

"""
Calculate whether the inputted year is a leap year.
"""


# Input the year
try:
    year = int(input())
except ValueError:
    print('Not a number')

if ((year % 2 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('YES')
else:
    print('NO')

