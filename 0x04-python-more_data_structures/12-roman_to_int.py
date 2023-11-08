#!/usr/bin/python3
def roman_to_int(roman_string):
    def roman_thousands(string):
        count = string.count("M") * 1000
        return count
    def roman_hundrads(string):
        count = 0
        for i in range(len(string)):
            if string[i] == 'C' and string[i - 1] != 'X':
                count += 100
            elif string[i] == 'D' and string[i - 1] == 'C':
                count += 300
            elif string[i] == 'D':
                count += 500
            elif string[i] == 'M' and string[i - 1] == 'C':
                count += 800
        return count
    def roman_tens(string):
        count = 0
        for i in range(len(string)):
            if string[i] == 'X' and string[i - 1] != 'I':
                count += 10
            elif string[i] == 'L' and string[i - 1] == 'X':
                count += 30
            elif string[i] == 'L':
                count += 50
            elif string[i] == 'C' and string[i - 1] == 'X':
                count += 80
        return count
    def roman_ones(string):
        count = 0
        for i in range(len(string)):
            if string[i] == 'I':
                count += 1
            elif string[i] == 'V' and string[i - 1] == 'I' and i != 0:
                count += 3
            elif string[i] == 'V':
                count += 5
            elif string[i] == 'X' and string[i - 1] == 'I' and i != 0:
                count += 8
        return count
    funcs = [roman_thousands, roman_hundrads, roman_tens, roman_ones]
    add = 0
    if (roman_string):
        for f in funcs:
            add += f(roman_string)
    return add
