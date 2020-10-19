# -*- coding: utf-8 -*-

"""
The length of the circle road is 109 km. Given: velocity, time.
Return coordinate of the moving object
by the given time and velocity.
"""

try:
    length = 7
    velocity = int(input('Velocity (km/h): '))
    time = int(input('Time (h): '))
    print((velocity*time)%length)
except ValueError:
    print('Incorrect input')
