#!/usr/bin/python3
"""
0. What's my status? #0
"""
from urllib import request
import sys

with request.urlopen(sys.argv[1]) as r:
    print(r.headers.__getitem__("X-Request-Id"))
