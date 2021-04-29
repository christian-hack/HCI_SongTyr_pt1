import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd

cid = "9828445b08644a13a067e7959d1a4b6d"
secret = "ca46715f11484acdac1036ae59e8b93e"

os.environ['SPOTIPY_CLIENT_ID']=cid
os.environ['SPOTIPY_CLIENT_SECRET']=secret
os.environ['SPOTIPY_REDIRECT_URI']='http://localhost:8888/callback'

username = ""
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope, show_dialog=True)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')
    for song in range(50):
        list = []
        list.append(results)
        with open('top50_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
    with open('top50_data.json') as f:
        data = json.load(f)

    list_of_results = data[0]["items"]
    list_of_artist_names = []
    list_of_artist_uri = []
    list_of_song_names = []
    list_of_song_uri = []
    list_of_durations_ms = []
    list_of_explicit = []
    list_of_albums = []
    list_of_popularity = []

    for result in list_of_results:
        result["album"]
        this_artists_name = result["artists"][0]["name"]
        list_of_artist_names.append(this_artists_name)
        this_artists_uri = result["artists"][0]["uri"]
        list_of_artist_uri.append(this_artists_uri)
        list_of_songs = result["name"]
        list_of_song_names.append(list_of_songs)
        song_uri = result["uri"]
        list_of_song_uri.append(song_uri)
        list_of_duration = result["duration_ms"]
        list_of_durations_ms.append(list_of_duration)
        song_explicit = result["explicit"]
        list_of_explicit.append(song_explicit)
        this_album = result["album"]["name"]
        list_of_albums.append(this_album)
        song_popularity = result["popularity"]
        list_of_popularity.append(song_popularity)

    all_songs = pd.DataFrame(
        {'artist': list_of_artist_names,
         'artist_uri': list_of_artist_uri,
         'song': list_of_song_names,
         'song_uri': list_of_song_uri,
         'duration_ms': list_of_durations_ms,
         'explicit': list_of_explicit,
         'album': list_of_albums,
         'popularity': list_of_popularity
     
         })

    all_songs_saved = all_songs.to_csv('top50_artists.csv')
else:
    print("Can't get token for", username)