from os import access
import requests

from api_setup import headers
from api_setup import BASE_URL

LIMIT = 50

# Returns list of track features from a list of playlist ids
def get_mood_tracks(playlist_ids):
    # List of tracks
    tracks = []

    # Set of track ids to keep track of used tracks
    id_set = set()

    # Compile list of tracks from playlists
    for id in playlist_ids:
        # GET request for tracks from a playlist
        playlist_response = requests.get(
                BASE_URL + 'playlists/' + id + '/tracks', 
                params={'limit': LIMIT},
                headers=headers
        ).json()

        # String of comma-separated track ids
        track_ids = ""

        # Put ids in the string of track ids
        for item in playlist_response['items']:
            # Check if the id has been used or not
            if item['track']['id'] not in id_set:
                track_ids += item['track']['id'] + ','
                id_set.add(item['track']['id'])
        
        # GET request for track features from track list
        tracks_response = requests.get(
            BASE_URL + 'audio-features',
            params={'ids': track_ids},
            headers=headers
        ).json()
        
        # Put track features in tracks list
        for track in tracks_response['audio_features']:
            tracks.append(track)
    
    return tracks


# Returns a list of features from a list of tracks
def get_feature_data(track_list, feature):
    # List of track_list's data on given feature
    feature_data = []
    for track in track_list:
        feature_data.append(track[feature])

    return feature_data

# Trims a list of data to remove outliers using either interquartile range (IQR) or standard deviation (SD)
def trim_data(data):
    # TODO: Decide whether to use IQR or SD
    # TODO: Implement this function
    pass
