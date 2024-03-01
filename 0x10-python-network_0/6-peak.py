#!/usr/bin/python3
"""
6. Find a peak
"""


def find_peak(array):
    """
    This function finds a peak in a list of unsorted integer
    """
    if not array or not len(array):
        return None
    lo = 0
    hi = len(array) - 1
    while hi >= lo:
        mid = lo + ((hi - lo) // 2)
        if mid < len(array) - 1 and array[mid + 1] >= array[mid]:
            lo = mid + 1
        elif mid > 0 and array[mid - 1] > array[mid]:
            hi = mid - 1
        else:
            return array[mid]
