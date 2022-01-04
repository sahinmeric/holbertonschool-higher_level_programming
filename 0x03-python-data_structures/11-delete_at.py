#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    new_list = my_list.copy()
    my_list.clear()
    for i in range(len(new_list)):
        if i == idx:
            continue
        else:
            my_list.append(new_list[i])
    return my_list
