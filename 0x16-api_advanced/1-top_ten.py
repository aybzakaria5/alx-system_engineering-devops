#!/usr/bin/python3
"""retriving top 10 posts drom a subbredit"""
import requests


def top_ten(subreddit):
    """a method to queries a given api and returns the top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headres = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headres, allow_redirects=False)
    if response.status_code == 200:
        all_posts = response.json()["data"]["children"]
        for count in range(10):
            print(all_posts[count]["data"]["title"])
    else:
        return ("None")
