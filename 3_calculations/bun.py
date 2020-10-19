# -*- coding: utf-8 -*-

"""
A bun costs a dollars and b cents.
This program prints number a and b for
n amount of buns.
"""


try:
    dollars = int(input('Dollars: '))
    cents = int(input('Cents (1-99): '))
    if cents < 1 or cents > 99:
        print('amount of cents has to be between 1 and 99')
    else:
        amount = int(input('How many: '))
        print(f'{dollars*amount + cents*amount//100}.{cents*amount%100}')
except ValueError:
    print('Input error')
