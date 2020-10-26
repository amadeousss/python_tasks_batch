# -*- coding: utf-8 -*-

"""
Kids are splitting apples from the basket.
This program calculates the integer amount of apples each kid gets.
Remainder is kept in the basket.
Output: Amount, Remainder
"""


try:
    children = int(input())
    apples = int(input())
    print(apples//children, apples%children)
except ValueError:
    print('Invalid input.')

