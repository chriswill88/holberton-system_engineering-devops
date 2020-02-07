#!/usr/bin/python3
import requests
import requests.auth


def number_of_subscribers(subreddit):
    # client_auth = requests.auth.HTTPBasicAuth('p-jcoLKBynTLew', 'gko_LXELoV07ZBNUXrvWZfzE3aI')
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    numOfUsers = 0
    headers = {'User-Agent': 'Python/requests'}
    red = requests.get(url, headers=headers, params={'raw_json': '1'})
    try:
        rdict = red.json()
    except Exception:
        return 0
    for i in rdict:
        if isinstance(rdict[i], dict):
            for x in rdict[i]:
                if x == 'subscribers':
                    numOfUsers = rdict[i][x]
                    break

    return numOfUsers
