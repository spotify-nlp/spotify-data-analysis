from utils import get_mood_tracks
from utils import analyze
import json

# List of fear playlist ids
fear_playlist_ids = [
    '5YGKIOyuR3kNQfMxUVO3l3',
    '3gs7IiEw2P1Ywlm7XWh7UG',
    '0WiqDvPh0oMMHYDHMAofe8',
    '5AM4lgcUAw5sokybXj3ny7',
    '1OA0au0fVXfHnD5l9ERASD',
    '17BEKaSMdvXq2Ep7HI3TQP',
    '0SC3OdbRPbD4byQVthLzDE',
    '37Dr3tkteguXQPMRUkYeoI',
]

# List of fear tracks
fear_tracks = get_mood_tracks(fear_playlist_ids)

print(json.dumps(analyze(fear_tracks), indent=4))
