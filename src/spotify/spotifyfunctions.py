import random
from .. import tokens as tokens
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import json


# Set authorization in CC flow
auth_manager = SpotifyClientCredentials(client_id=tokens.get_spotify_clientid(),
                                        client_secret=tokens.get_spotify_secretid())
sp_client = spotipy.Spotify(auth_manager=auth_manager)


def update_TrBl2():
    # Setting a scope for CAC flow
    playlistscope = "playlist-modify-public"
    # Get CAC authorized variable
    sp_auth = spotipy.Spotify(
        auth_manager=SpotifyOAuth(client_id=tokens.get_spotify_clientid(),
                                  client_secret=tokens.get_spotify_secretid(),
                                  redirect_uri=tokens.get_redirect_uri(),
                                  scope=playlistscope))

    scraped_songs = dict()
    song_count = 0

    # iterate through all the people we have
    for person in tokens.dataDict:
        # check that the person game me the links I've asked for 4 times and counting
        if(tokens.get_person_data(person, 'onrepeat') is not None and tokens.get_person_data(person, 'repeatrewind') is not None):
            # get the On Repeat playlist data dump
            on_repeat = sp_client.playlist_items(
                tokens.get_person_data(person, 'onrepeat'), fields=None, limit=50, offset=0, market='US')
            # get the size of the On Repeat playlist
            playlist_size = on_repeat['total']
            # divde that so we can get an even number of songs per participant
            divisor = playlist_size//3
            # randomly choose some track numbers to pick from OR
            ORrands = [random.randint(0, divisor-1), random.randint(
                divisor, divisor*2-1), random.randint(divisor*2, playlist_size-1)]
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
                tokens.get_person_data(person, 'repeatrewind'), fields=None, limit=50, offset=0, market='US')
            # get the size of the Repeat Rewind playlist
            playlist_size = repeat_rewind['total']
            # divde that so we can get an even number of songs per participant
            divisor = playlist_size//2
            # randomly choose some track numbers to pick from RR
            RRrands = [random.randint(0, divisor-1),
                       random.randint(divisor, playlist_size-1)]
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
        tokens.get_TribeBlend2_ID(), tracklist)

    print(scraped_songs)

# this function is not used. it is simply for testing purposes


def output_playlist_info():
    # change the spotipy method here to test object output
    tribeblend = sp_client.playlist_items(tokens.get_TribeBlend2_ID())
    # print results to a formatted file for viewing. (file is gitignored)
    with open('playlist_output', 'w') as playlist_output:
        json.dump(tribeblend, playlist_output, indent=4, sort_keys=True)
