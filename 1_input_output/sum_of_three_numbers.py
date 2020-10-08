# -*- coding: utf-8 -*-

"""This program returns sum of 3 numbers from the input"""

try:
    print(sum([int(input()) for i in range(3)]))
except:
    print('Error')
