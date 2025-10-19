#!/usr/bin/python3
"""
Python script to export an employee's TODO list data in JSON format.
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch user and TODO list data for a given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    return user_info, todos_info


def export_to_json(employee_id, username, todos):
    """
    Export TODO list data to a JSON file named '<employee_id>.json'.
    """
    todos_data = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    data = {str(employee_id): todos_data}

    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./export_to_json.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_info, todos_info = fetch_employee_data(employee_id)
    username = user_info.get("username")
    export_to_json(employee_id, username, todos_info)
