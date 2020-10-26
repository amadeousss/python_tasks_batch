# -*- coding: utf-8 -*-

"""
This program calculates amount of desks needed for 3 classes.
One desk is used not more than by 2 students.
Input: number of students in each of every class.
Output: number of desks overall.
"""


try:
    # Amount of children in each class
    kids_list = [int(input()) for i in range(3)]

    # Number of desks needed for every class
    print(sum([-(kids//-2) for kids in kids_list]))
except ValueError:
    print('Invalid input.')

