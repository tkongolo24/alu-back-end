#!/usr/bin/python3
"""Script to gather employee TODO list progress from REST API"""
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
    employee_name = user_data.get("name")

    # Get employee's TODO list
    todos_response = requests.get(f"{base_url}/todos",
                                   params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)

    todos = todos_response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display results
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
