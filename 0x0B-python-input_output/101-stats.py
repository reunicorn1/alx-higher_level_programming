#!/usr/bin/python3
"""
This is a script which supplies multiple functions to log parse
"""
import sys


total_size = 0
code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def log(status_code, size):
    """This function logs data from each line of the stimulated HTTP
    GET request for /project/260

    Args:
       status_code (str)
       size (str)
    """
    global total_size
    global code
    total_size += int(size)
    code[int(status_code)] += 1


def flush():
    """This function prints data existing into the stdout in a certain
    format
    """
    global total_size
    global code
    print("File size: {}".format(total_size))
    for key in sorted(code):
        if code[key] == 0:
            pass
        else:
            print("{}: {}".format(key, code[key]))

def validate_line(line):
    if len(line) != 9:
        return False
    IP_address = list(map(lambda x: int(x), line[0].split('.')))
    if not all(num < 256 and num > 0 for num in IP_address):
        return False
    if line[1] != "-" and line[4] != '"GET' and line[5] != "/projects/260":
        return False
    if line[6] != 'HTTP/1.1"':
        return False
    if int(line[7]) not in [200, 301, 400, 401, 403, 404, 405, 500]:
        return False
    if not (int(line[8]) < 1025 and int(line[8]) > 0):
        return False
    return True

n = 0
try:
    for line in sys.stdin:
        size, status_code = line.split()[-1], line.split()[-2]
        if validate_line(line.split()):
            log(status_code, size)
            n += 1
        if (n % 10 == 0):
            flush()
    flush()
except KeyboardInterrupt as e:
    flush()
    raise e
