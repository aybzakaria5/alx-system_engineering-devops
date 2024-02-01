#!/usr/bin/python3
"""Gather data from an API and export to JSON."""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/".format(url)

    "Get user's info"
    resp = requests.get(user_url)
    users = resp.json()

    all_res = {}
    for usr in users:
        task_arr = []
        "Get user's info"
        username = usr.get("username")

        data_url = "{}/todos?userId={}".format(url, usr.get("id"))
        "Get user's todos"
        resp = requests.get(data_url)
        todos = resp.json()
        for task in todos:
            task_dict = {}
            task_dict["username"] = username
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_arr.append(task_dict)

        all_res[usr.get("id")] = task_arr

    all_res = json.dumps(all_res)

    with open("todo_all_employees.json", "w") as file:
        file.write(all_res)
