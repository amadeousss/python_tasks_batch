# -*- coding: utf-8 -*-

"""
A bun costs a dollars and b cents.
This program prints number a and b for
n amount of buns.
"""


try:
    dollars = int(input('Dollars: '))
    cents = int(input('Cents (1-99): '))
except ValueError:
    print('Input error')
if cents < 1 or cents > 99:
    raise Exception('Inputted amount of cents is less than 1 or more than 99')
amount = int(input('How many: '))
print(f'{dollars*amount + cents*amount//100}.{cents*amount%100}')
