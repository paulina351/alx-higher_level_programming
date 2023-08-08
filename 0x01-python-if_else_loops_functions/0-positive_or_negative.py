#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
x = int(input("please enter an integer: "))
if x > 0:
    print('{} is positive')
elif x == 0:
    print('{} is zero')
else:
    print('{} is negative')
