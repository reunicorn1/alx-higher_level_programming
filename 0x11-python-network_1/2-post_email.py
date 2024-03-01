#!/usr/bin/python3
"""
2. POST an email #0
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode("utf-8"))
