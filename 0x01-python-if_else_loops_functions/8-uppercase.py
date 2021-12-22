#!/usr/bin/python3
def uppercase(str):
    for a in str:
        i = ord(a)
        if i > 96 and i < 123:
            i = i - 32
            a = chr(i)
        else:
            a = chr(i)
        print(a, end="")
    print("\n")
