from bs4 import BeautifulSoup
import requests
from api import CLIENT_ID, CLIENT_SECRET, REDIRECT_ULR
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which Year you want to travel to? Type Date in this format: YYYY-MM-DD:")
year = date.split("-")[0]

response = requests.get(f"https://appbrewery.github.io/bakeboard-hot-100/{date}/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

song_tags = soup.select('h3.chart-entry__title')
song_names = [song.get_text(strip=True) for song in song_tags]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_ULR,
                                                scope="playlist-modify-private",
                                                show_dialog=True,
                                                cache_path="Day-46//token.txt"
                                                ))

# i made a mistake here that i was using h3 > chart-entry_title i forgot about underscore and selectors rule
song_names = soup.select('h3.chart-entry__title')

song_data = []

for song in song_names:
    song_data.append(
        {
            "Text": song.get_text(strip=True)
        }
    )

user_id = sp.current_user()["id"]
print(f"Successfully authenticated as user: {user_id}")
song_uris = []
print("\nSearching for songs on Spotify...")

for song in song_names:
    search_query = f"track:{song} year:{year}"
    result = sp.search(q=search_query, type="track", limit=1)
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        try:
            fallback_result = sp.search(q=f"track:{song}", type="track", limit=1)
            uri = fallback_result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"'{song}' couldn't be found on Spotify. Skipping.")

print(f"Found {len(song_uris)} out of {len(song_names)} songs.")

if song_uris:
    playlist_name = f"{date} Billboard Hot 100"
    
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    playlist_id = playlist["id"]
    
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
    print(f"\nSuccess! Your playlist '{playlist_name}' has been created.")
else:
    print("\nNo songs were found, so no playlist was created.")