#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        b = list(my_list)
        if not (idx >= len(my_list) or idx < 0):
            b[idx] = element
        return b
