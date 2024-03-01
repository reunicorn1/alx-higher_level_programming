#!/usr/bin/python3
"""
6. Find a peak
"""

def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integer
    """
    if not list_of_integers or not len(list_of_integers):
        return None
    lo = 0
    hi = len(list_of_integers) - 1
    while hi >= lo:
        mid = lo + ((hi - 1) // 2)
        if mid < len(list_of_integers) - 1 and list_of_integers[mid + 1] >= list_of_integers[mid]:
            lo = mid + 1
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            hi = mid - 1
        else:
            return list_of_integers[mid]
