import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

cid = '3fffcfb44a32410aa1a7d89d343345cb'
secret = '57860c20b80d47ecae4ea486b71db6ec'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist = sp.artist("2ARH58Hit3yC6ziGdhma23")
track = sp.track("70UbxfwWbeiglv4hbKcDz7")
album = sp.album("5XpHo23Du4H9scYqGxLUIJ")
pprint.pp(artist)