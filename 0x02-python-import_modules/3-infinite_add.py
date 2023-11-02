#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summing = 0
    for num in sys.argv[1:]:
        summing += int(num)
    print(summing)
