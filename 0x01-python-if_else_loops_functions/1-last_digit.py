#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    cpynumber = number * -1
cpynumber = number
last_digit = cpynumber % 10
_string = ""
if last_digit > 5:
    _string = "and is greater than 5"
elif last_digit < 6 and last_digit > 0:
    _string = "and is less than 6 and not 0"
else:
    _string = "and is 0"
print("Last digit of {} is {} {}".format(number, last_digit, _string))
