# File to store track data for different moods, just so that we aren't re-making API calls every time we want to do something
# Note that ideally the track lists are generated once and then messed with elsewhere

from os import access

from utils import get_mood_tracks
from utils import get_feature_data

sad_playlist_id = '6nxPNnmSE0d5WlplUsa5L3'

# List of sad playlist ids
sad_playlist_ids = [
    '6nxPNnmSE0d5WlplUsa5L3',
    '4yXfnhz0BReoVfwwYRtPBm',
    '3c0Nv5CY6TIaRszlTZbUFk'
]

# List of sad tracks
sad_tracks = get_mood_tracks(sad_playlist_ids)

print(len(sad_tracks))

print(get_feature_data(sad_tracks, 'energy'))
