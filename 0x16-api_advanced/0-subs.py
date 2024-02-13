#!/usr/bin/python3
"""module to retrive the number of subscribers on a subnet using reddit API"""
import requests

url = "https://www.reddit.com/r/{}/about.json"
def number_of_subscribers(subreddit):
    """function to get the number of subscribers on a subreddit"""
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url.format(subreddit), headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
