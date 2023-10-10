#!/usr/bin/python3
"""This script conatins a function that
queries the reddit API for a subreddit and
returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """This function queries the reddit API
    for the number of subscribers to a particular
    subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "0-subs"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    reddits = r.json()
    return reddits["data"].get("subscribers")
