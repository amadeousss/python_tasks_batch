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

# The algorithm, create new list in main list if current element is
# not equal to the last one.
result = []
previous_element = ''
index = -1
for current_element in source_list:
    if current_element != previous_element:
        index += 1
        result.append([])
    result[index].append(current_element)

print(result)
