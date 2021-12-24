#!/usr/bin/python3
from sys import argv
argc = len(argv) - 1
arg_str = ""
if argc == 1:
    arg_str = "argument"
else:
    arg_str = "arguments"
if __name__ == "__main__":
    if argc == 0:
        print("{} {}.".format(argc, arg_str))
    else:
        print("{} {}.".format(argc, arg_str))
        for i in argv:
            if argc != 0:
                print("{:d}: {:s}".format(i, argv[i]))

