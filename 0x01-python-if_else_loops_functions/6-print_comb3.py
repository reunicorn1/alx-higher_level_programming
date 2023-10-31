#!/usr/bin/python3
start = 1
for i in range(8):
    for j in range(start, 10):
        print("{}{}, ".format(i, j), end="")
    start += 1
print("89")
