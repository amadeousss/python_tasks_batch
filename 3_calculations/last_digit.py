# -*- coding: utf-8 -*-

"""
This program outputs last digit of given natural number
"""


try:
    number = int(input())
    print(number % 10)
except ValueError:
    print('Incorrect input')
