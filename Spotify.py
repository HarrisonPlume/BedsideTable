# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:06:02 2021

@author: Plume
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

os.environ["SPOTIPY_CLIENT_ID"]= "bdd78b08a3c2462eb1c9c9f047133ec3"
os.environ["SPOTIPY_CLIENT_SECRET"]="8d4e63a17c7c4b33971dad89fdd84aee"
os.environ["SPOTIPY_REDIRECT_URI"]="http://www.google.com/"

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

User = sp.current_user()
DisplayName = User["display_name"]

print(DisplayName)

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])