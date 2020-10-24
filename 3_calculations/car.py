# -*- coding: utf-8 -*-

"""
The car goes n kilometres per day. This program
calculates amound of days needed to make m kilometres.
"""


try:
    velocity = float(input("Velocity (km/day): "))
    kilometres = float(input("kilometres (km): "))
except ValueError:
    print('The input is not a number. Type a number.')

# double negative is made to ceil the division.
print(-(-kilometres//velocity))
