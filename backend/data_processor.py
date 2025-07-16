# data_processor.py
import re
from collections import Counter

def extract_music_mentions(comments):
    # Simple regex for "Artist - Song" format
    pattern = re.compile(r'(.+?)\s*[-–]\s*(.+)')
    mentions = []

    for comment in comments:
        matches = pattern.findall(comment)
        for match in matches:
            mentions.append(f"{match[0].strip()} - {match[1].strip()}")

    return Counter(mentions)

