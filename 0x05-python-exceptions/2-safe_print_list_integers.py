#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nmb = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            nmb += 1
    except:
        continue
    finally:
        print()
    return nmb
