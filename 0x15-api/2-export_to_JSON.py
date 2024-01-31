#!/usr/bin/python3
""" a script to retrive some data about users using theire given id"""
import json
import requests
from sys import argv


def get_employee_todo_tasks(employee_id):
    """ a methode to retrive the current situation about
    a user's tasks tracking"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todo_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_endpoint)
    if user_response.status_code != 200:
        print("Unable to retrieve user data. Status code: {}"
              .format(user_response.status_code))
        return

    user_data = user_response.json()
    # getting thz username
    userName = user_data.get("username")
    # getting the user id
    userId = user_data.get("id")
    # creating a json file inforamt userid.json
    filename = "{}.json".format(userId)

    # Fetch todo data
    todo_response = requests.get(todo_endpoint)
    if todo_response.status_code != 200:
        print("Unable to retrieve todo data. Status code: {}"
              .format(todo_response.status_code))
        return

    todo_data = todo_response.json()
    # getting the data about todos
    # tracking_tasks = todo_data.get("completed")
    # creating the data to get wrote in the json file
    json_data = {str(userId): [{"task": task.get('title'), "completed":
                 task.get('completed'), "username": userName} for task in
                 todo_data]}

    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Employee {} tasks exported successfully to {}"
          .format(userName, filename))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_tasks(employee_id)
