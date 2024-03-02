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
        if not r.json():
            print("No result!")
        else:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON ")
