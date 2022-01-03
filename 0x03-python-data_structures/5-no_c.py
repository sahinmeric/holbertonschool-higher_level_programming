#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            continue
        new_list.append(letter)
    new_string = ""
    for i in range(len(new_list)):
        new_string += new_list[i]
    return new_string
