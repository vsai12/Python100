from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "bd329509526a4851944571b168aae19b"
CLIENT_SECRET = "f111be20ea504cb6b6da010f415c0744"

REDIRECT_URI = "http://example.com"

user_date = input("Which year do you want too travel to? Type the date in this format YYYY-MM-DD: ")

resp = requests.get(f"{URL}/{user_date}")
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
html_song_titles = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in html_song_titles]
# first_artist = soup.select_one(
#     "li ul li span[class=\"c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
#     "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
#     "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only "
#     "u-font-size-20@tablet\"]").get_text().strip()
# html_artists = soup.select("li ul li span[class=\"c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
#                            "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
#                            "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only\"]")
# artists = [artist.get_text().strip() for artist in html_artists]
# artists.insert(0, first_artist)

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        show_dialog=True,
        cache_path="token.txt",
        username="Tetsuya Kagami")
    )

user_id = spotify.current_user()["id"]
year = user_date.split("-")[0]
song_uris = []
for ind in range(100):
    result = spotify.search(q=f"track:{song_names[ind]} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(result)
        print(f"{song_names[ind]} doesn't exist in Spotify. Skipped.")

playlist = spotify.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)