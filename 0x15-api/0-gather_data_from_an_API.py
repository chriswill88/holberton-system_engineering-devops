#!/usr/bin/python3
import requests
import sys
"""parses info from api"""

if __name__ == "__main__":
    idE = int(sys.argv[1])
    # this pulls up the posts
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    listy = r.json()
    for i in listy:
        if i['id'] == idE:
            rightdict = i
            break
    EMPLOYEE_NAME = rightdict["name"]
    title_list = []
    a = requests.get('https://jsonplaceholder.typicode.com/todos')
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    listy = a.json()
    for i in listy:
        if i['userId'] == idE:
            TOTAL_NUMBER_OF_TASKS += 1
            if i["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1
                title_list.append(i["title"])

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS))
    for title in title_list:
        TASK_TITLE = "\t {}".format(title)
        print(TASK_TITLE)
