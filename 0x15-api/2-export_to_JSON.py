#!/usr/bin/python3
"""Export user data to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

    user = requests.get(user_url).json()
    username = user.get("username")

    todos = requests.get(todos_url).json()

    list_of_tasks = []
    for task in todos:
        completed = task.get("completed")
        title = task.get("title")
        data = {"username": username, "task": title, "completed": completed}
        list_of_tasks.append(data)

    with open("{}.json".format(id), mode="w") as f:
        json.dump({id: list_of_tasks}, f)
