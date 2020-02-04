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

    userlist = r.json()
    todolist = a.json()

    thedict = {}
    prev = []

    for i in userlist:
        USER_ID = i['id']
        USERNAME = i["username"]
        num = 0
        datalist = []
        if USER_ID not in prev:
            for x in todolist:
                if x["userId"] == USER_ID:
                    TASK_TITLE = x["title"]
                    TASK_COMPLETED_STATUS = x["completed"]
                    datalist.append({})
                    datalist[num]["username"] = USERNAME
                    datalist[num]["task"] = TASK_TITLE
                    datalist[num]["completed"] = TASK_COMPLETED_STATUS
                    num += 1
                thedict[str(USER_ID)] = datalist
        prev.append(USER_ID)
    with open('todo_all_employees.json'.format(USER_ID), 'w') as e:
        json.dump(thedict, e)
