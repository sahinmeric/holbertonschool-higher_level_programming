#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz ", end="")
            continue
        if i % 3 == 0:
            print("Fizz ", end="")
            continue
        if i % 5 == 0:
            print("Buzz ", end="")
            continue
        else:
            print("{:d} ".format(i), end="")

fizzbuzz()
