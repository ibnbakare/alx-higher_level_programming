#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_dig = int(str(number)[-1])
if number < 0:
    print(f"Last digit of {number} is -{last_dig} and is less than 6 and not 0")
elif last_dig > 5:
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
elif last_dig == 0:
    print(f"Last digit of {number} is {last_dig} and is 0")
