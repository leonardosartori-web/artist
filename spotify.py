import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '3fffcfb44a32410aa1a7d89d343345cb'
secret = '57860c20b80d47ecae4ea486b71db6ec'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def searchQuery(query, typeS):
    data = sp.search(query, 5, 0, typeS)[typeS + "s"]["items"][0]["external_urls"]["spotify"]
    return data