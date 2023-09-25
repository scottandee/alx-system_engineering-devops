#!/usr/bin/python3
"""Record all tasks from all users"""

import json
import requests


if __name__ == "__main__":
    all_user_tasks = {}

    # Get total number of users
    users = requests.get("https://jsonplaceholder.typicode.com/users/")
    num_of_users = len(users.json())

    # Iterate through all users
    for i in range(1, num_of_users):
        id = str(i)

        user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

        user = requests.get(user_url).json()
        username = user.get("username")

        todos = requests.get(todos_url).json()

        # Make a list of todos for the current iteration of user
        list_of_user_tasks = []
        for task in todos:
            completed = task.get("completed")
            title = task.get("title")
            d = {"username": username, "task": title, "completed": completed}
            list_of_user_tasks.append(d)

        # Add the user and his todos to dictionary of all users
        all_user_tasks[id] = list_of_user_tasks

    # Convert the dictionary of users and their todos into JSON
    with open("todo_all_employees.json", mode="w") as f:
        json.dump(all_user_tasks, f)
