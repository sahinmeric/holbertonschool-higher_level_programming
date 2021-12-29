#!/usr/bin/python3
def remove_char_at(str, n):
    cpy_str = ""
    len_str = len(str)
    for i in range(len_str):
        if i != n:
            cpy_str += str[i]
    return(cpy_str)
