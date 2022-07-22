import random
from .. import localtokens as localtokens
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import json


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
                localtokens.get_person_data(person, 'repeatrewind'), fields=None, limit=50, offset=0, market='US')
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
        localtokens.get_TribeBlend2_ID(), tracklist)

    print(scraped_songs)


def count_playlist_artists(playlistID):
    # get the playlist items
    playlist = sp_client.playlist_items(playlistID, limit=100)
    playlistSize = playlist["total"]
    # Starting empty dictionary to hold what I want
    artistCountDict = {}

    loopcount = 0
    while playlistSize > 0:
        playlist = sp_client.playlist_items(
            playlistID, limit=100, offset=100*loopcount)
        # For every single item (song) in the playlist
        for item in playlist["items"]:
            # Hold the track dictionary
            track = item["track"]
            # For every artist listed in the track, pull the details
            for artist in track["artists"]:
                artistName = artist["name"]
                artistID = artist["id"]

                # If the artist doesn't exist, add it
                if artistID not in artistCountDict:
                    artistCountDict[artistID] = {
                        "artistName": artistName,
                        "count": 1
                    }
                else:
                    artistCountDict[artistID]["count"] += 1
        loopcount += 1
        playlistSize -= 100

    # Sort the final dictionary to make it easier to find the max
    return sort_artist_dict(artistCountDict)


def sort_artist_dict(artistDict):
    # Given the dictionary...
    sortedDict = sorted(
        artistDict.items(),
        # Sorting by count
        key=lambda x: x[1]["count"],
        # Descending order
        reverse=True
    )
    return sortedDict


def get_playlist_name(playlistID):
    playlist = sp_client.playlist(playlistID)
    return playlist["name"]


# this function is not used. it is simply for testing purposes
def output_playlist_info():
    # change the spotipy method here to test object output
    tribeblend = sp_client.playlist_items(localtokens.get_TribeBlend2_ID())
    # print results to a formatted file for viewing. (file is gitignored)
    with open('playlist_items_output', 'w') as playlist_output:
        json.dump(tribeblend, playlist_output, indent=4, sort_keys=True)
    tribeback = sp_client.playlist(localtokens.get_TribeBlend2_ID())
    # print results to a formatted file for viewing. (file is gitignored)
    with open('playlist_output', 'w') as playlist_output:
        json.dump(tribeback, playlist_output, indent=4, sort_keys=True)
