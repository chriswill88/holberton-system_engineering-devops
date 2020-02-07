#!/usr/bin/python3
"""This modual contains top_ten functions"""
import requests


def recurse(subreddit, hot_list=[], next=None, count=0):
    """This Function queries from the reddit api"""
    # print("count! -> {}\nnext = {}".format(count, next))
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    numOfUsers = 0
    headers = {"User-Agent": "ChangeMeClient/0.1 by Chris"}

    red = requests.get(url, headers=headers, params={'after': next})

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
                # print(i, x, rdict[i][x])
                if x == "children":
                    childs = rdict[i][x]
                    break

    i = 0
    while i < len(childs):
        hot_list.append("{}".format(childs[i]['data']['title']))
        i += 1
    # x = 0
    # for i in hot_list:
    #     print("title[{}] ->{}".format(x, i))
    #     x += 1
    if rdict['data']['after']:
        nexty = rdict['data']['after']
        recurse(subreddit, hot_list, nexty, count + 1)
    return hot_list

# recurse("programming")
