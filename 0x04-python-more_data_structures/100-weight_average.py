#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list):
        total = sum(value_1 * value_2 for value_1, value_2 in my_list)
        sub_total = sum(value_2 for _, value_2 in my_list)
        return float(total / sub_total)
