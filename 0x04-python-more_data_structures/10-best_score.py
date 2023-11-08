#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        swiped = {value: key for key, value in a_dictionary.items()}
        values = list(swiped.keys())
        values.sort()
        highest = values[-1]
        return swiped[highest]
