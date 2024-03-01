#!/usr/bin/python3
"""
8. Search API
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        print("{} {}".format(r.json()['id'], r.json()['name']))
    except requests.exceptions.JSONDecodeError as e:
        if e == 'Expecting value: line 1 column 1 (char 0)':
            print('No result')
        else:
            print('Not a valid JSON')
