# test_data_processor.py
from backend import data_processor

def test_extract_music_mentions():
    sample_comments = [
        "Radiohead - Creep",
        "I love Billie Eilish – Bad Guy",
        "Queen - Bohemian Rhapsody"
    ]
    result = data_processor.extract_music_mentions(sample_comments)
    assert result["Radiohead - Creep"] == 1

