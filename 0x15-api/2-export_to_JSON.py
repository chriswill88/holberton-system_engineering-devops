#!/usr/bin/python3
"""parses info from api"""
import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = int(sys.argv[1])
    USERNAME = ""
    TASK_COMPLETED_STATUS = ""
    TASK_TITLE = ''
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    listy = r.json()
    for i in listy:
        if i['id'] == USER_ID:
            rightdict = i
            break
    USERNAME = rightdict["username"]
    title_list = []
    a = requests.get('https://jsonplaceholder.typicode.com/todos')
    listy = a.json()
    licty = []
    newdict = {str(USER_ID): licty}
    num = 0
    for i in listy:
        if i['userId'] == USER_ID:
            TASK_TITLE = i["title"]
            TASK_COMPLETED_STATUS = str(i["completed"])
            licty.append({})
            licty[num]["task"] = TASK_TITLE
            licty[num]["completed"] = TASK_COMPLETED_STATUS
            licty[num]["username"] = USERNAME
            num += 1
    with open(str(USER_ID) + '.json', 'w') as e:
        json.dump(newdict, e)
