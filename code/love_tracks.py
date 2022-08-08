from utils import get_mood_tracks
from utils import analyze
import json

# List of love playlist ids
love_playlist_ids = [
    '3pVgPrVzMMn9EOur2Zwtgj',
    '0nevMyChAKVxX6sGwby5A6',
    '4cJ8qUzt5CSTE9XN5uK2z2',
    '2p6SAq9WHFaodqizQ0TTdO',
    '37i9dQZF1DX7rOY2tZUw1k',
    '37i9dQZF1DX38lOuCWlLV1',
    '37i9dQZF1DWSlwBojgQEcN',
    '37i9dQZF1DWYMvTygsLWlG',
]

# List of love tracks
love_tracks = get_mood_tracks(love_playlist_ids)

print(json.dumps(analyze(love_tracks), indent=4))
