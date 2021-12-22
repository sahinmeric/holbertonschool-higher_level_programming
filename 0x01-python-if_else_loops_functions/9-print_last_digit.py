#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number < 0:
        number = number * -1
        last_digit = number % 10
        return (last_digit)
    elif number > 0:
        last_digit = number % 10
        return (last_digit)
    else:
        return (last_digit)
