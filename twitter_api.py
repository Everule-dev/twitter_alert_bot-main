# twitter_api.py

import requests

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJgVuwEAAAAA1rZ0oM4ZWuOtNnEc7QNi2mEl3Yw%3DWKzEuPTeUxN3mOGBWGOpIrDgJywbwuGNWJ1PWV2Tbmse2lkJRA"

def get_tweet_count(keyword):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {"query": keyword, "max_results": 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return len(response.json().get("data", []))
    else:
        print("Twitter API error:", response.status_code, response.text)
        return 0
