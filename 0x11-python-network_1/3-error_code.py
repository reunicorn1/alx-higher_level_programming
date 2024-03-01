#!/usr/bin/python3
"""
3. Error code #0
"""
from urllib import request
import urllib
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
