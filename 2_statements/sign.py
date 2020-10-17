# -*- coding: utf-8 -*-

"""
This program determines sign of an inputted number
"""


try:
    number = int(input('Input a number: '))
except ValueError:
    print('Not a number')

print((number>0) - (number<0))
