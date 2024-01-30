#!/usr/bin/python3
"""using api to retrive some informations about a user using theire id"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_Id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    usr_endpoint = "{}/users/{}".format(url, employee_Id)
    todo_url = "{}/todos?userId={}".format(url, employee_Id)

    # checking status about users
    req_0 = requests.get(usr_endpoint)
    if req_0.status_code != 200:
        print("unable to retrive the data , the satatu is {}"
              .format(req_0.status_code))
        exit(1)
    # retriving the employee name if the statu is 200
    usr_name = req_0.json().get("name")
    # checking status about todos
    req_1 = requests.get(todo_url)
    if req_1.status_code != 200:
        print("unable to retrive data about todos,the statu is {}"
              .format(req_1.status_code))
        exit(1)
    # retriving the completed tasks
    todo_data = req_1.json()
    len_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if
                       (task.get("completed") == True)]
    # the url will be then like :
    # https://jsonplaceholder.typicode.com/todos?userId=2&completed=True
    len_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(usr_name, len_completed_tasks, len_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
    print(todo_data)
