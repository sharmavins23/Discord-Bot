import random
from .. import localtokens as localtokens
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


# Set authorization in CC flow
auth_manager = SpotifyClientCredentials(client_id=localtokens.get_spotify_clientid(),
                                        client_secret=localtokens.get_spotify_secretid())
sp_client = spotipy.Spotify(auth_manager=auth_manager)


def update_TrBl2():
    # Setting a scope for CAC flow
    playlistscope = "playlist-modify-public"
    # Get CAC authorized variable
    sp_auth = spotipy.Spotify(
        auth_manager=SpotifyOAuth(client_id=localtokens.get_spotify_clientid(),
                                  client_secret=localtokens.get_spotify_secretid(),
                                  redirect_uri=localtokens.get_redirect_uri(),
                                  scope=playlistscope))

    scraped_songs = dict()
    song_count = 0

    # iterate through all the people we have
    for person in localtokens.dataDict:
        # check that the person game me the links I've asked for 4 times and counting
        if(localtokens.get_person_data(person, 'onrepeat') is not None and localtokens.get_person_data(person, 'repeatrewind') is not None):
            # get the On Repeat playlist data dump
            on_repeat = sp_client.playlist_items(
                localtokens.get_person_data(person, 'onrepeat'), fields=None, limit=50, offset=0, market='US')
            # randomly choose some track numbers to pick from OR
            ORrands = [random.randint(0, 9), random.randint(
                10, 19), random.randint(20, 29)]
            # iterate through the track list pulled from the playlist
            for idx, item in enumerate(on_repeat['items']):
                # if this track is one of our randomly picked ones, lets save it
                if idx in ORrands:
                    song_count += 1  # incrememnt our counter for the big dict
                    track = item['track']
                    # save some info about this track; we'll use this later
                    track_info = {
                        "Title": track['name'],
                        "ID": track['id'],
                        "Added By": str(person),
                        "Pulled From": 'On Repeat'
                    }
                    # update the dictionary of the songs we're pulling
                    scraped_songs.update(
                        {f"Track {song_count}": track_info})

            # get the Repeat Rewind playlist data dump
            repeat_rewind = sp_client.playlist_items(
                localtokens.get_person_data(person, 'repeatrewind'), fields=None, limit=50, offset=0, market='US')
            # randomly choose some track numbers to pick from RR
            RRrands = [random.randint(0, 14), random.randint(15, 29)]
            # iterate through the track list pulled from the playlist
            for idx, item in enumerate(repeat_rewind['items']):
                # if this track is one of our randomly picked ones, lets save it
                if idx in RRrands:
                    song_count += 1  # incrememnt our counter for the big dict
                    track = item['track']
                    # save some info about this track; we'll use this later
                    track_info = {
                        "Title": track['name'],
                        "ID": track['id'],
                        "Added By": str(person),
                        "Pulled From": 'Repeat Rewind'
                    }
                    # update the dictionary of the songs we're pulling
                    scraped_songs.update(
                        {f"Track {song_count}": track_info})

    tracklist = list()
    for track in scraped_songs:
        tracklist.append(scraped_songs[track]["ID"])

    # get our scraped songs and put them into a playlist
    sp_auth.playlist_replace_items(
        localtokens.get_TribeBlend2_ID(), tracklist)

    print(scraped_songs)
