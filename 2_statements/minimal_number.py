# -*- coding: utf-8 -*-

"""
This program prints out the least of two
inputted numbers
"""


try:
    first_number = int(input())
    second_number = int(input())
    if first_number == second_number:
        print(f"They are equal. {first_number}")
    elif first_number < second_number:
        print(first_number)
    else:
        print(second_number)
except ValueError:
    print('Invalid input')

