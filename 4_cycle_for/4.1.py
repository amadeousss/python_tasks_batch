# -*- coding: utf-8 -*-

"""
Print all numbers between A and B
"""


try:
    a = int(input())
    b = int(input())
except ValueError:
    print('Incorrect input')

for i in range(a, b+1):
    print(i)
