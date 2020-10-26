# -*- coding: utf-8 -*-

"""
Given nmber of minutes passed from the start of the day,
get correct amount of hours (from 0 to 23) passed
and minutes (from 0 to 59).
"""


try:
    total_minutes = int(input())
    hours = (n//60)%24
    minutes = n%60
    print(hours, minutes)
except ValueError:
    print('Invalid input.')

