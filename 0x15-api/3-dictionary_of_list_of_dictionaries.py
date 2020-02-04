#!/usr/bin/python3
"""parses info from api"""
import json
import requests

if __name__ == "__main__":
    USER_ID = ""
    USERNAME = ""
    TASK_COMPLETED_STATUS = ""
    TASK_TITLE = ''
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    a = requests.get('https://jsonplaceholder.typicode.com/todos')
    listy = r.json()
    newdict = {}

    for i in listy:
        USER_ID = str(i['id'])
        USERNAME = i["username"]
        listy = a.json()
        licty = []
        num = 0
        for i in listy:
            TASK_TITLE = i["title"]
            TASK_COMPLETED_STATUS = str(i["completed"])
            licty.append({})
            licty[num]["username"] = USERNAME
            licty[num]["task"] = TASK_TITLE
            licty[num]["completed"] = TASK_COMPLETED_STATUS
            num += 1
        newdict[str(USER_ID)] = licty

    with open('todo_all_employees.json'.format(USER_ID), 'w') as e:
        json.dump(newdict, e)
