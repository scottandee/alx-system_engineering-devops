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

    with open("{}.csv".format(id), mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos:
            completed = task.get("completed")
            title = task.get("title")
            row = [id, username, completed, title]
            csv_writer.writerow(row)
