#!/usr/bin/python3
""" a recursive function that queries the Reddit API and returns a list
using parameter after to get the next page in the API response"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """ a recursive function that queries the Reddit API and returns a list"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'Mozilla/5.0 '}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
