#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = float(a / b)
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {f}".format((a / b)))
    return res
