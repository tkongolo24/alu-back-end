#!/usr/bin/python3
"""Script to export all employees TODO list data to JSON format"""
import json
import requests


if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get("{}/users".format(base_url))
    if users_response.status_code != 200:
        exit(1)

    users = users_response.json()

    # Get all todos
    todos_response = requests.get("{}/todos".format(base_url))
    if todos_response.status_code != 200:
        exit(1)

    todos = todos_response.json()

    # Create a dictionary to map user IDs to usernames
    user_dict = {}
    for user in users:
        user_dict[user.get("id")] = user.get("username")

    # Build the JSON structure
    all_employees_data = {}

    for user_id, username in user_dict.items():
        # Filter todos for this user
        user_todos = [todo for todo in todos
                      if todo.get("userId") == user_id]

        # Build task list for this user
        tasks_list = []
        for task in user_todos:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        # Add to main dictionary with user_id as string key
        all_employees_data[str(user_id)] = tasks_list

    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(all_employees_data, jsonfile)
