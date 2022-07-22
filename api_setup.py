from os import access
import requests

CLIENT_ID = '9e00882f3a16400aadb1b35e035a341c'
CLIENT_SECRET = 'cc046a91fa1f43978b16b0189511ea4b'

AUTH_URL = 'https://accounts.spotify.com/api/token'


auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})

access_token = auth_response.json()['access_token']

headers = {
    'Authorization': f'Bearer {access_token}'
}

BASE_URL = 'https://api.spotify.com/v1/'
