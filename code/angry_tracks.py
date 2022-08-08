from utils import get_mood_tracks
from utils import analyze
import json

# List of angry playlist ids
angry_playlist_ids = [
    '5bWn8XcgI3hv2vpWjNq8la',
    '1WJSCv94LinHIjb0kLx5a6',
    '1mxhSTG1EST8AyJGepJkPV',
    '5O12S9z3O8dEhHWt3bPbxm',
    '15Glcc8LdAloMFFfbODCl7',
    '1GQN1sURUr0jFVJ8fYFBOH',
    '5OHv3aqXBXWjxsyCAYJpeu',
    '4ZkCaz5hzzbNBitvk57O6r',
]

# List of angry tracks
angry_tracks = get_mood_tracks(angry_playlist_ids)

print(json.dumps(analyze(angry_tracks), indent=4))
