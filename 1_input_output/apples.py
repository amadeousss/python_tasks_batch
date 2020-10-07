# -*- coding: utf-8 -*-
#Kids are splitting apples from the basket. This program calculates the integer
#amount of apples each kid gets if there are k apples and n children.
#Remainder is kept in the basket. Output: Amount, Remainder
n = int(input())
k = int(input())
print(k//n, k%n)
