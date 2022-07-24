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
