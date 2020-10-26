# -*- coding: utf-8 -*-

"""
This program gets an input list and then splits it into several lists,
all consisting of equal numbets.
"""


# Get an input list
source_list = []
size = int(input("Number of elements in list: "))
for i in range(size):
    source_list.append(int(input()))

# Sort the list
source_list.sort()

# The algorithm: create new sublist in main list if current element is
# not equal to the last one in the last sublist.
result = [[source_list[0]]]
for el in source_list[1:]:
    if el != result[-1][-1]:
        result.append([])
    result[-1].append(el)

print(result)

