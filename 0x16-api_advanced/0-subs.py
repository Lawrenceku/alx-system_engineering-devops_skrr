#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get, exceptions


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, return 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = get(url, headers=user_agent, allow_redirects=False)
        # Check for successful response
        if response.status_code != 200:
            return 0
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    except (exceptions.RequestException, ValueError):
        return 0
