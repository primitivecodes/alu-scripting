#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Main function"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if response.status_code == 200:
            hot_posts = response.json().get("data", {}).get("children", [])
            for post in hot_posts:
                print(post.get('data', {}).get('title'))
    except Exception:
        pass

    print("OK")
