#!/usr/bin/env python3
""" a script to retrive some data about users using theire given id"""
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
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
    employee_name = user_data.get("name")

    # Fetch todo data
    todo_response = requests.get(todo_endpoint)
    if todo_response.status_code != 200:
        print("Unable to retrieve todo data. Status code: {}"
              .format(todo_response.status_code))
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    completed_tasks = [tsk["title"] for tsk in todo_data if tsk["completed"]]

    # Display information
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed_tasks), total_tasks))
    for task_title in completed_tasks:
        print(f"\t {task_title}")


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
