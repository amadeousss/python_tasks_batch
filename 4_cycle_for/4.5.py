# -*- coding: utf-8 -*-

"""
Given number 'n', print following sum: '1! + 2! + 3! + ... + n!'
"""


try:
    n = int(input('n: '))
except ValuError:
    print('Incorrect input')

factorial = 1
sum = 1

for i in range(2, n+1):
    factorial *= i
    sum += factorial

print(factorial, sum)
