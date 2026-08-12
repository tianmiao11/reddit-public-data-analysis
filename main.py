import os
import praw

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="python:reddit-public-data-analysis:v0.1"
)

subreddit = reddit.subreddit("travel")

for post in subreddit.new(limit=10):
    print({
        "title": post.title,
        "score": post.score,
        "num_comments": post.num_comments,
        "created_utc": post.created_utc,
        "url": post.url
    })
