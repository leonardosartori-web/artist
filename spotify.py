import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

cId = "3fffcfb44a32410aa1a7d89d343345cb"
cs = "57860c20b80d47ecae4ea486b71db6ec"
client_credentials_manager = SpotifyClientCredentials(client_id=cId, client_secret=cs)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist = sp.user_follow_artists(["4NVhhX3tA4m84EqNNSOJV2"])
pprint.pp(artist)