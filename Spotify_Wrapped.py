import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os 
import pprint
import pandas as pd

scope = 'user-top-read, user-read-currently-playing'
client_id = 'FILL IN'
client_secret = 'FILL IN'
redirect_uri = 'https://localhost/'

time_range = 'short_term'
limit = 15

def switch(time_range):
    if time_range == 'short_term':
        return 'SHORT TERM'
    elif time_range == 'medium_term':
        return 'MEDIUM TERM'
    elif time_range == 'long_term':
        return 'LONG_TERM'

sp2 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
tracks = sp2.current_user_top_tracks(limit=limit, time_range=time_range)

artists = sp2.current_user_top_artists(limit=limit,time_range=time_range)
#print(type(results))

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(tracks)

tracks_df = pd.DataFrame.from_dict(tracks)
artists_df = pd.DataFrame.from_dict(artists)

#pp.pprint(sp2.currently_playing())
print('\n\n')
print('*' * 30)
print(f'TOP {limit} {switch(time_range)} TRACKS')
print('*' * 30)

for el in tracks['items']:
    print(el['name'])

print('\n')
print('*' * 30)
print(f'TOP {limit} {switch(time_range)} ARTISTS')
print('*' * 30)

for el in artists['items']:
    print(el['name'])

print('\n\n')
