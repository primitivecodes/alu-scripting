#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-Reddit-App/0.1"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print(None)
            return

        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
