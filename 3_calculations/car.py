# -*- coding: utf-8 -*-

"""
The car goes n kilometres per day. This program
calculates amound of days needed to make m kilometres.
"""

try:
    velocity = float(input("Velocity (km/day): "))
    kilometres = float(input("kilometres (km): "))
    print(-(-kilometres//velocity))
except ValueError:
    print('Incorrect input')
