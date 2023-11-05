#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    str_list = [x for x in str_list if x not in "cC"]
    new_str = "".join(str_list)
    return new_str
