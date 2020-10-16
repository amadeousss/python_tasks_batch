# -*- coding: utf-8 -*-

"""
This program returns the number going before and after the given one.
"""

try:
    n = int(input())
    print(f'The next number for the number {n} is {n+1}.')
    print(f'The previous number for the numbers {n} is {n-1}.')
except ValueError:
    print('Invalid input.')
