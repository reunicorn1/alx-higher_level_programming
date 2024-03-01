#!/usr/bin/python3
"""
0. What's my status? #0
"""
from urllib import request


with request.urlopen('https://alx-intranet.hbtn.io/status') as r:
    html = r.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode("utf-8"))
