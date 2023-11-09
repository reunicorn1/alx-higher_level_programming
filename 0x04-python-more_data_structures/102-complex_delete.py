#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cancelled = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            cancelled.append(key)
    for item in cancelled:
        a_dictionary.pop(item)
    return a_dictionary
