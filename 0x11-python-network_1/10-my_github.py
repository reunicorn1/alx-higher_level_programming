#!/usr/bin/python3
"""
9. My GitHub!
"""
import requests
import sys


if __name__ == "__main__":
    head = {'read': 'user', 'Authorization': 'token {}'.format(sys.argv[2])}
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    r = requests.get(url, headers=head)
    print(r.json().get('id'))
