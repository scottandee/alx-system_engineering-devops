#!/usr/bin/python3
"""This script gathers data from an API"""

import requests
import sys


user_url = "https://jsonplaceholder.typicode.com/users/"


def gather_data(id):
    """This function gathers all information of a
    user using the id passed
    """
    users = requests.get(user_url).json()

    # Retreive employee name with user id passed
    name = ""
    for user in users:
        if user.get("id") == id:
            name = user.get("name")
            break

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    todos = requests.get(todos_url).json()
    tots_num_of_tasks = len(todos)

    # Count number of completed tasks
    num_of_done = 0
    completed = []
    for task in todos:
        if task.get("completed") is True:
            num_of_done = num_of_done + 1
            completed.append(task)

    print(f"Employee {name} is done with \
tasks({num_of_done}/{tots_num_of_tasks}):")
    for task in completed:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    gather_data(int(sys.argv[1]))
