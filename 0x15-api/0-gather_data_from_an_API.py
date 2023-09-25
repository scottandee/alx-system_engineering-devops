#!/usr/bin/python3
"""This script gathers data from an API"""

import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]

    # Retreive employee name with employee id passed
    res = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}")
    details = res.json()
    emp_name = details.get("name")

    # Get a list of done tasks, find the length
    res = requests.get(f"""https://jsonplaceholder.typicode.com/\
todos?userId={emp_id}&completed=true""")
    completed = res.json()
    num_of_done = len(completed)

    # Get the total number of tasks done
    res = requests.get(f"""https://jsonplaceholder.typicode.com/\
todos?userId={emp_id}""")
    all_tasks = res.json()
    tots_num_of_tasks = len(all_tasks)

    print(f"Employee {emp_name} is done with tasks({num_of_done}\
/{tots_num_of_tasks})")
    for task in completed:
        print("\t {}".format(task.get("title")))
