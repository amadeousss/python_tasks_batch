# -*- coding: utf-8 -*-

"""
Given 3 numbers calculate how many of them are equal:
3 - if all are equal
2 - if two are equal
0 - if each one is different
"""


numbers = []
i = 0
while i < 3:
    try:
        numbers.append(int(input('Input a number: ')))
        i += 1
    except ValueError:
        print('Not a number!')

if (len(set(numbers)) == 1):
    print(3)
elif (len(set(numbers)) == 2):
    print(2)
else:
    print(0)
