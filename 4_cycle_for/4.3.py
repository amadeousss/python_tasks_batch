# -*- coding: utf-8 -*-

"""
Given number A and B (A>B), print every odd number
between them inclusively in reversed order.
"""


try:
    A = int(input("A: "))
    B = int(input("B: "))
except ValueError:
    print("Incorrect input.")

# A-(1-A%2) return A if A is odd, return A-1 if A is even. This way we start
# the loop with an odd number. B-B%2 is needed because loop stops before
# iterator becomes equal to B, so we need to make B smaller by 1 if it's odd.
for i in range(A-(1-A%2), B-B%2, -2):
    print(i)

