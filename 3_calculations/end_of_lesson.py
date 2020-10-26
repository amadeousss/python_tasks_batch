# -*- coding: utf-8 -*-

"""
This program, given a number of the lesson, returns
the numbers which tell when the lesson is over.
"""


try:
    number = int(input('Type a number between 1 and 10: '))
except ValueError:
    print('Input error')

if 1 <= number <= 10:

    # (number//2) returns amount of odd number between 1 and number inclusively.
    # (number-1)//2) return amound of even numbers between 1 and number
    # inclusively.
    minutes = (number//2)*5 + ((number-1)//2)*15 + number*45 + 9*60
    print(f'{minutes//60}:{minutes%60}')
else:
    print(f'{number} is not between 1 and 10!')

