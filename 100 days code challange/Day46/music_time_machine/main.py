import requests, spotipy, os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

# API DOCS LINK https://spotipy.readthedocs.io/en/2.25.0/, https://developer.spotify.com

# This program uses web scraping to get the top 100 songs of a specific date from the billboard website and uses the spotify API to create a playlist with those songs

# To use just input the date in the format (YYYY-MM-DD) and the program will create a playlist with the top 100 songs of that date
# The playlist will be created in your spotify account and will be private
# Or you can input the playlist id and the program will add the songs to that playlist

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")

# date = "2000-08-12"
date = input("Enter the date in the format (YYYY-MM-DD): ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = f'https://www.billboard.com/charts/hot-100/{date}/'

def create_music_dict():
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    music_list =  [music.getText().strip() for music in soup.select(selector="div ul li ul li h3")]
    artist_list = [artist.getText().strip() for artist in soup.select(selector="div ul li ul li span.a-no-trucate.a-font-primary-s")]
    return dict(zip(music_list, artist_list))

def create_playlist():
    playlist_name = f"{date} Billboard 100"
    playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False)
    with open(f"{playlist_name}.txt", "w") as file:
        file.write(f"Playlist id: {playlist["id"]}\nUser id: {user_id}\Billboard url: {url}")
    id = playlist["id"]
    return id

def add_to_playlist():
    # search for the track
    id = input("Enter the playlist id or enter 'create': ")
    if id == "create":
        playlist_id = create_playlist()
    else:
        playlist_id = id
    for music in music_dict:
        try:
            m_response = spotify.search(q=f"track:{music} artist:{music_dict[music]}", type="track")
            spotify.playlist_add_items(playlist_id= playlist_id ,items=[m_response["tracks"]["items"][0]["uri"]], position=None)
            print(f"Added {music} by {music_dict[music]}")
        except Exception as e:
            with open(f"error_report.txt", "a") as file:
                file.write(f"{e}\n")
            print(e)

music_dict = create_music_dict()
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:1234", scope="playlist-modify-private", 
                                                    show_dialog=True, cache_path="token.txt", ))
user_id = spotify.current_user()["id"]

add_to_playlist()