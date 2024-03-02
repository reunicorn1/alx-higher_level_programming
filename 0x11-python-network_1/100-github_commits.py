#!/usr/bin/python3
"""
10. Time for an interview!
"""
import requests
import sys


if __name__ == "__main__":
    head = {'Accept': 'application/vnd.github+json'}
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url, headers=head)
    for data in r.json():
        print("{} {}".format(data['sha'], data['commit']['author']['name']))
