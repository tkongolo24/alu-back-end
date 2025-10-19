#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID.
"""

import json
import requests
from sys import argv


def fetch_employee_data(employee_id):
    """
    Fetch employee information and their TODO list from the API.
    """
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(base_url)
    todos_response = requests.get(f"{base_url}/todos")

    employee = employee_response.json()
    todos = todos_response.json()

    return employee, todos


def display_todo_progress(employee, todos):
    """
    Display the progress of an employee's TODO list.
    """
    employee_name = employee.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
    else:
        employee_id = argv[1]
        employee, todos = fetch_employee_data(employee_id)
        display_todo_progress(employee, todos)
