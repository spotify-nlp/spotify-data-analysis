from utils import get_mood_tracks
from utils import analyze
import json

# List of sad playlist ids
sad_playlist_ids = [
    '6nxPNnmSE0d5WlplUsa5L3',
    '4yXfnhz0BReoVfwwYRtPBm',
    '3c0Nv5CY6TIaRszlTZbUFk',
    '1MNjeV3vCsk4TEQ2tiKQss',
    '37i9dQZF1DWSqBruwoIXkA',
    '5FeHyyiioSObGs9mIVqW5b',
    '37i9dQZF1DWYfVqUciU2jI',
    '37i9dQZF1DX7qK8ma5wgG1',
    '37i9dQZF1DWVrtsSlLKzro',
    '70VaOHyjpsWcmA4gxosExZ',
    '3k5RqaLqjsw48wsb2KjGtQ',
    '6AA8CZHoMLs0A2vwrNMLdC',
    '4QgNA28tONdhtb7zJMNz6I',
    '4mpUNBP40eDTcv0CdtqHAv',
    '0zHkISuEcNr2Zav2X4TXCQ',
    '0HBS2rm9P4tDra7GWYE6Qd',
    '6O1ZnUG2mtmeEqxxPa5OWn',
    '5uNwbizUHsctoLUV4KPHMn'
]

# List of sad tracks
sad_tracks = get_mood_tracks(sad_playlist_ids)

print(json.dumps(analyze(sad_tracks), indent=4))
