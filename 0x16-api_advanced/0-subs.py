#!/usr/bin/python3
"""This modual contains number_of_subscribers functions"""
import requests


def number_of_subscribers(subreddit):
    """This Function queries from the reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    numOfUsers = 0
    headers = {'User-Agent': 'Python/requests'}
    red = requests.get(url, headers=headers, params={'raw_json': '1'})
    if red.status_code != 200:
        return 0
    rdict = red.json()
    for i in rdict:
        if isinstance(rdict[i], dict):
            for x in rdict[i]:
                if x == 'subscribers':
                    numOfUsers = rdict[i][x]
                    break
    return numOfUsers
