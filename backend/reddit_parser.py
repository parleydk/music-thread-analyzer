# reddit_parser.py
import praw

def fetch_comments(thread_url):
    # TODO: Replace with your Reddit API credentials
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='music-thread-analyzer'
    )

    submission = reddit.submission(url=thread_url)
    submission.comments.replace_more(limit=0)
    comments = [comment.body for comment in submission.comments]
    return comments

