#!/usr/bin/python3
"""
Python script to export an employee's TODO list data in CSV format.
"""

import csv
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


def export_to_csv(employee_id, username, todos):
    """
    Export TODO list data to a CSV file named '<employee_id>.csv'.
    """
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./export_to_csv.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_info, todos_info = fetch_employee_data(employee_id)

    username = user_info.get("username")
    export_to_csv(employee_id, username, todos_info)
