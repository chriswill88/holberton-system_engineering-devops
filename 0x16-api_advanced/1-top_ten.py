#!/usr/bin/python3
"""This modual contains top_ten functions"""
import requests


def top_ten(subreddit):
    """This Function queries from the reddit api"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    numOfUsers = 0
    headers = {"User-Agent": "ChangeMeClient/0.1 by Chris"}
    red = requests.get(url, headers=headers, params={"limit": 10})
    # print(red)
    # print(red.text)
    if red.status_code != 200:
        print("None")
        return
    try:
        rdict = red.json()
    except Exception:
        print("None")
        return
    # print(rdict)
    for i in rdict:
        # print(i)
        if isinstance(rdict[i], dict):
            for x in rdict[i]:
                if x == "children":
                    childs = rdict[i][x]
                    break

    i = 0
    while i < len(childs):
        print("{}".format(childs[i]['data']['title']))
        i += 1
