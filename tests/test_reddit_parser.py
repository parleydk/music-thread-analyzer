# test_reddit_parser.py
from backend import reddit_parser

def test_fetch_comments():
    # This test assumes a valid Reddit URL and credentials
    comments = reddit_parser.fetch_comments("https://www.reddit.com/r/Music/comments/example_thread/")
    assert isinstance(comments, list)

