# -*- coding: utf-8 -*-

import math

"""
This program calculates amount of desks needed for 3 classes.
One desk is used not more than by 2 students.
Input: number of students in each of every class.
Output: number of desks overall.
"""

try:
    # Amount of children in each class
    kids1 = int(input())
    kids2 = int(input())
    kids3 = int(input())

    # Number of desks needed for every class
    print(sum([math.ceil(kids/2) for kids in [kids1, kids2, kids3]]))
except ValueError:
    print('Invalid input.')
