#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i != j and j > i:
            c = str(i) + str(j)
            c = int(c)
            if c == 89:
                print("{0:0=2d}".format(c))
            else:
                print("{0:0=2d}, ".format(c), end="")
