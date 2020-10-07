# -*- coding: utf-8 -*-
#This program calculates amount of desks needed for 3 classes. One desk is
#used not more than by 2 students. Input: number of students in each of
#every class. Output: number of desks overall.
import math
num1 = int(input()) #amount of children in first class
num2 = int(input())
num3 = int(input())
desks1 = math.ceil(num1/2) #number of desks needed for first class
desks2 = math.ceil(num2/2)
desks3 = math.ceil(num3/2)
print(desks1 + desks2 + desks3)
