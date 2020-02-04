#!/usr/bin/python3
import csv
import requests
import sys
"""parses info from api"""

if __name__ == "__main__":
    USER_ID = int(sys.argv[1])
    USERNAME = ""
    TASK_COMPLETED_STATUS = ""
    TASK_TITLE = ''
    # this pulls up the posts
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
    # with open('{}.csv'.format(USER_ID), 'w', newline='') as e:
    # write = csv.writer(e)
    newlist = []
    for i in listy:
        if i['userId'] == USER_ID:
            TASK_TITLE = i["title"]
            TASK_COMPLETED_STATUS = str(i["completed"])
            newlist.append([
                '{}'.format(USER_ID),
                '{}'.format(USERNAME),
                '{}'.format(TASK_COMPLETED_STATUS),
                '{}'.format(TASK_TITLE)])

    with open('{}.csv'.format(USER_ID), 'w', newline='') as e:
        write = csv.writer(e, quoting=csv.QUOTE_ALL, quotechar='\"')
        write.writerows(newlist)
