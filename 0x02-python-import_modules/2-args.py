#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = "argument" if len(sys.argv) == 2 else "arguments"
    delim = "." if len(sys.argv) == 1 else ":"
    print("{} {}{}".format(len(sys.argv) - 1, arg, delim))
    count = 1
    for char in sys.argv[1:]:
        print("{}: {}".format(count, char))
        count += 1
