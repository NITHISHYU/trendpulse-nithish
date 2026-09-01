"""
TrendPulse - Task 1: Data Collection

Fetches live trending stories from the Hacker News public API
and saves the raw data to trends_raw.csv.
"""

import time
import requests
import pandas as pd

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
NUMBER_OF_STORIES = 30


def get_json(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def collect_trending_data(limit=NUMBER_OF_STORIES):
    story_ids = get_json(TOP_STORIES_URL)[:limit]
    rows = []

    for rank, story_id in enumerate(story_ids, start=1):
        story = get_json(ITEM_URL.format(story_id))

        if not story or story.get("type") != "story":
            continue

        rows.append({
            "rank": rank,
            "id": story.get("id"),
            "title": story.get("title"),
            "score": story.get("score", 0),
            "comments": story.get("descendants", 0),
            "author": story.get("by"),
            "url": story.get("url"),
            "time": story.get("time"),
            "collected_at": pd.Timestamp.now(tz="UTC").isoformat()
        })

        time.sleep(0.05)

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = collect_trending_data()
    df.to_csv("trends_raw.csv", index=False)

    print(f"Collected {len(df)} trending stories.")
    print("Saved: trends_raw.csv")
