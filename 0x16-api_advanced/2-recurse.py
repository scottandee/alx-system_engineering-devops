#!/usr/bin/python3
"""This script contains a function that
returns a list containing the titles of all
hot articles for a specified subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """This function creates a list of all hot
    articles recursively
    """
    # Base Case
    if after is None:
        return

    # Check if the recurse function is called for the first time
    if after == "":
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    # Query the url
    headers = {"User-Agent": "2-recurse"}
    r = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is a valid one
    if r.status_code != 200:
        print("None")
        return

    # Get the next page identifier and call the recurse function with it
    dic = r.json()
    next_page = dic["data"]["after"]
    li = recurse(subreddit, hot_list, next_page)

    if li is not None:
        hot_list = li

    # Get the array of posts and its length for the current page
    arr_posts = dic["data"]["children"]
    posts_len = dic["data"]["dist"]

    # Append to list
    for i in range(posts_len):
        hot_list.append(arr_posts[i]["data"].get("title"))

    return hot_list
