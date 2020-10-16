# -*- coding: utf-8 -*-

"""
User inputs 4 number: 2 are coordinates of first figure
on chess table, other 2 - ones for the second figure.
Program calculates whether both of the figures stand on
squares of the same color.
"""

coordinates = []
for i in range(4):
    try:

        #input coordinate
        coordinate = int(input('Number between 1 and 8 inclusive: '))
    except ValueError:
        print('Not a number')

        #check if coordinate in range of 1 and 8 inclusive
    if not (1 <= coordinate <= 8):
        raise Exception('Not a number between 1 and 8 inclusive')
    coordinates.append(coordinate)

print('YES') if (sum(coordinates) % 2 == 0) else print('NO')
