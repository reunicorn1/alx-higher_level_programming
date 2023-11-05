#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def tuple_checker(tup=()):
        if len(tup) == 0:
            return 0, 0
        elif len(tup) == 1:
            return tup[0], 0
        return tup
    a = tuple_checker(tuple_a)
    b = tuple_checker(tuple_b)
    c = (a[0] + b[0], a[1] + b[1])
    return c
