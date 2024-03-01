#!/usr/bin/python3
"""
1. Response header value #0"
"""
from urllib import request
import sys

with request.urlopen(sys.argv[1]) as r:
    print(r.headers.get("X-Request-Id"))
