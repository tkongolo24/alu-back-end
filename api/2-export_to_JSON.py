#!/usr/bin/python3
"""Script to export employee TODO list data to JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    try:
        employee_id = sys.argv[1]
        user_id = int(employee_id)
    except (ValueError, IndexError):
        sys.exit(1)

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    if user_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Get employee's TODO list
    todos_response = requests.get("{}/todos".format(base_url),
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)

    todos = todos_response.json()

    # Build JSON structure
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Create final JSON object
    json_data = {employee_id: tasks_list}

    # Write to JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, mode='w') as jsonfile:
        json.dump(json_data, jsonfile)
