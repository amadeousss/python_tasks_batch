# -*- coding: utf-8 -*-

"""
This program return area of a right triangle, legs of which are inputted.
"""


try:
    first_leg = int(input())
    second_leg = int(input())
    print(first_leg*second_leg*0.5)
except ValueError:
    print('Invalid input.')
