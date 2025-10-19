#!/usr/bin/python3
"""
Python script to gather data from an API and export all employees'
TODO list information into a single JSON file.
"""

import json
import requests


def get_employee_tasks(employee_id):
    """
    Fetch TODO list data for a given employee ID.
    Returns a list of task dictionaries.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    username = user_info.get("username")

    return [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos_info
    ]


def get_all_employee_ids():
    """
    Fetch all employee IDs from the API.
    Returns a list of IDs.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    users_info = requests.get(url).json()
    return [user.get("id") for user in users_info]


if __name__ == "__main__":
    all_employees = {}
    employee_ids = get_all_employee_ids()

    for emp_id in employee_ids:
        all_employees[str(emp_id)] = get_employee_tasks(emp_id)

    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(all_employees, jsonfile, indent=4)
