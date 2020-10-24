# -*- coding: utf-8 -*-

"""
Given number 'n', get its factorial.
"""


try:
    n = int(input('n: '))
except ValueError:
    print('Incorret input')

factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)
