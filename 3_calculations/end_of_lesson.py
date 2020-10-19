# -*- coding: utf-8 -*-

"""
This program, given a number of the lesson, returns
the numbers which tell when the lesson is over.
"""


try:
    number = int(input('Type a number between 1 and 10: '))
    if 1 <= number <= 10:
        minutes = (number//2)*5 + ((number-1)//2)*15 + number*45 + 9*60
        print(f'{minutes//60}:{minutes%60}')
    else:
        print('Number has to be between 1 and 10')
except ValueError:
    print('Input error')
