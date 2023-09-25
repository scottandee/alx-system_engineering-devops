#!/usr/bin/python3
"""Gather data from an API and export to csv"""

import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

    user = requests.get(user_url).json()
    username = user.get("username")

    todos = requests.get(todos_url).json()
    # data is the dictionary that will be passed to the csv writer
    data = {"id": id, "username": username, "completed": "", "title": ""}

    with open("{}.csv".format(id), mode="w") as csv_file:
        fieldnames = data.keys()
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        for task in todos:
            data["completed"] = task.get("completed")
            data["title"] = task.get("title")
            csv_writer.writerow(data)
