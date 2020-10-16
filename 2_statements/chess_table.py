# -*- coding: utf-8 -*-

"""
User inputs 4 number: 2 are coordinates of first figure
on chess table, other 2 - ones for the second figure.
Program calculates whether both of the figures stand on
squares of the same color.
"""


coordinates = []
i = 0
while i < 4:
    try:
        coordinate = int(input('Print a number: '))
        if coordinate in range(1, 9):
            coordinates.append(coordinate)
            i += 1
        else:
            print('Not valid number. Try again.')
    except ValueError:
        print('Not a number.')

print('YES') if (sum(coordinates) % 2 == 0) else print('NO')
