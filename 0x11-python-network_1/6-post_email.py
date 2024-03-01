#!/usr/bin/python3
"""
5. Response header value #1
"""
import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
