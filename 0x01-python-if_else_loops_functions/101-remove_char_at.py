#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        str_cpy = str[:n] + str[n + 1:]
        return str_cpy
    else:
        return str
