# -*- coding: utf-8 -*-

"""
Print all numbers from A to B or
from B to A in reversed order.
"""


try:
    a = int(input())
    b = int(input())
except ValueError:
    print('Input error')

# (-1 + 2*int(a<b)) returns 1, if a<b; -1, if a>b.
# it represents step value of for loop,
for i in range(a, b-1 + 2*int(a<b), -1 + 2*int(a<b)):
    print(i)

