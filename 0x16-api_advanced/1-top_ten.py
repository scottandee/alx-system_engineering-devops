#!/usr/bin/python3
"""This script contains a function that
queries the reddit API and prints the titles
of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """This function queries the reddit API and
    prints the titles of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "1-top_ten"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print("None")
        return

    dic = r.json()
    posts = dic.get("data").get("children")

    for i in range(10):
        title = posts[i]["data"].get("title")
        print(title)
