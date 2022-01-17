#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nmb = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            nmb +=1
    except:
        pass
    finally:
        print()
    return nmb 
