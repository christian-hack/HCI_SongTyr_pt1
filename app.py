from flask import Flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import json

app = Flask(__name__)


app.secret_key = "ca46715f11484acdac1036ae59e8b93e"
app.config['SESSION_COOKIE_NAME'] = 'Christians Cookie'
TOKEN_INFO = "token_info"

@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code =request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getTopLists', _external=True))


@app.route('/getTracks')
def getTracks():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect("/")
    sp = spotipy.Spotify(auth = token_info['access_token'])
    all_songs = []
    iteration = 0
    while True:
        items = sp.current_user_saved_tracks(limit = 50, offset = iteration * 50)['items']
        iteration += 1
        all_songs += items
        if (len(items) < 50):
            break
    return str(len(all_songs))

@app.route('/getTopLists')
def getTopLists():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect("/")
    sp = spotipy.Spotify(auth = token_info['access_token'])
    results = sp.current_user_top_tracks(limit=50, offset = 0, time_range='long_term')
    for song in range(50):
        list = []
        list.append(results)
        with open('top50_LOLdata.json', 'w', encoding='utf-8') as f:
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

    s_tier_songs = []
    a_tier_songs = []
    b_tier_songs = []
    c_tier_songs = []
    d_tier_songs = []
    f_tier_songs = []
    for i in range(0,8):
        s_tier_songs.append(list_of_song_names[i])
    for i in range(8, 16):
        a_tier_songs.append(list_of_song_names[i])
    for i in range(16,24):
        b_tier_songs.append(list_of_song_names[i])
    for i in range(24, 34):
        c_tier_songs.append(list_of_song_names[i])
    for i in range(34,42):
        d_tier_songs.append(list_of_song_names[i])
    for i in range(42, 50):
        f_tier_songs.append(list_of_song_names[i])
    
    return (", ".join(list_of_song_names))

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if (is_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "9828445b08644a13a067e7959d1a4b6d",
        client_secret = "ca46715f11484acdac1036ae59e8b93e",
        redirect_uri=url_for('redirectPage', _external=True),
        scope="user-top-read")