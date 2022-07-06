import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
import pprint

client_id = "f2528356e4da4155a436c9edbdde361b"
client_secret = "aba03e41b2bc4f0f83ff75e7bbb461ed"

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getIdFromDict(artist_name):
    artists = {"YOASOBI": "64tJ2EAv1R6UaZqc4iOCyj",
               "B'z": "7i9bNUSGORP5MIgrii3cJc",
               "安室奈美恵": "4BmWSGKG6HiYvLuJvZ9afa",
               "宇多田ヒカル": "7lbSsjYACZHn1MSDXPxNF2",
               "ピンク・レディー": "4LE86GiUcfzELNnJrkmiGV",
               "石原裕次郎": "4wfj1VUQXlpBDbkXHkc6s6",
               "SKE48": "5G8OLQcvoCxiMQzwEcuWeN",
               "ザ・ドリフターズ": "1H1vWaQhd8vtdVRob9HEWv",
               "DREAMS COME TRUE": "2mJOGcLR3aCHkM1uAF93or",
                }
    artist_id = artists.get(artist_name, None)
    return artist_id


def getIdByArtist(artist_name):

    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id


def getTopSongs(artist_name):
    dict = {}
    try:
        # id = getIdByArtist(artist_name)
        id = getIdFromDict(artist_name)
        tracks = spotify.artist_top_tracks(id, country="JP")["tracks"]

        ids = []

        for track in tracks:
            id = track["id"]
            ids.append(id)

        features = spotify.audio_features(ids)
        for i, (feature, track) in enumerate(zip(features, tracks)):
            dict[i+1] = {"name": track["name"],
                         "image": track["album"]["images"][0]["url"],
                         "popularity": track["popularity"],
                         "preview_url": track["preview_url"],
                         "acousticness" : feature["acousticness"],
                         "danceability" : feature["danceability"],
                         "energy" : feature["energy"],
                         "instrumentalness" : feature["instrumentalness"],
                         "liveness" : feature["liveness"],
                         "speechiness" : feature["speechiness"],
                         "valence" : feature["valence"],
                         }
        
        
    except:
        print("error")

    return dict

if __name__ == "__main__":
    pprint.pprint(getTopSongs("B'z"))
