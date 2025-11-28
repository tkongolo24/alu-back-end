#!/usr/bin/python3
"""Script to export employee TODO list data to CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Get employee's TODO list
    todos_response = requests.get(f"{base_url}/todos",
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)

    todos = todos_response.json()

    # Write to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])
