from utils import get_mood_tracks
from utils import analyze
import json

# List of happy playlist ids
happy_playlist_ids = [
    '0RH319xCjeU8VyTSqCF6M4',
    '37i9dQZF1DXdPec7aLTmlC',
    '7GhawGpb43Ctkq3PRP1fOL',
    '37i9dQZF1DX1WSnLRtI26o',
    '37i9dQZF1DWZKuerrwoAGz',
    '0OOYm7ZTSB2ARCNuJkbLMh',
    '37i9dQZF1DX0UrRvztWcAU',
    '4AnAUkQNrLKlJCInZGSXRO',
]

# List of happy tracks
happy_tracks = get_mood_tracks(happy_playlist_ids)

print(json.dumps(analyze(happy_tracks), indent=4))
