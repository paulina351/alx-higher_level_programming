#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
x = int(input())
print("please enter a number: ", end="")

if x > 0:
    print("" + str(x) + " is positive")
elif x == 0:
    print("" + str(x) + " is zero")
else:
    print("" + str(x) + " is negative")
