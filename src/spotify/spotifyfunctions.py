from datetime import datetime
import random
from .. import tokens as tokens
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import json
import os
import psycopg2


class BotCacheHandler(spotipy.CacheHandler):
    """
    Handles reading and writing cached Spotify authorization tokens
    as json values in environment variable.
    """

    def get_cached_token(self):
        db_conn = None
        token_info = None

        try:
            # Connect to the DB
            db_conn = psycopg2.connect(
                tokens.get_database_url(), sslmode='require')
            # Set the cursor
            cur = db_conn.cursor()
            # SELECT the values we want
            cur.execute(
                """
                SELECT auth_token
                FROM spotify_auth_tokens
                WHERE discord_id = %s;
                """,
                (tokens.get_person_data('Pragosh', 'id'),))
            # Pull the top output row
            row = cur.fetchone()
            if row is None:
                # Since there's no DB auth token, let's use the config var
                token_info = json.loads(os.environ['SPOTIPY_AUTH_CACHE'])
                # Let's also put this config var token into the DB now
                cur.execute(
                    """
                    INSERT INTO spotify_auth_tokens (auth_token, discord_id, updated_date)
                    VALUES (%s, %s, %s);
                    """,
                    (os.environ['SPOTIPY_AUTH_CACHE'], tokens.get_person_data('Pragosh', 'id'), datetime.now()))
                # Save the changes
                db_conn.commit()
            else:
                # Turn the value of in the tuple into json
                token_info = json.loads(row[0])
            # Close the cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db_conn is not None:
                db_conn.close()

        return token_info

    def save_token_to_cache(self, token_info):
        db_conn = None
        # Make our token a json object to be sure
        new_token = json.dumps(token_info)

        try:
            # Connect to the DB
            db_conn = psycopg2.connect(
                tokens.get_database_url(), sslmode='require')
            # Set the cursor
            cur = db_conn.cursor()
            # UPDATE the values we want
            cur.execute(
                """
                UPDATE spotify_auth_tokens
                SET auth_token = %s, discord_id = %s, updated_date = %s
                """,
                (new_token, tokens.get_person_data('Pragosh', 'id'), datetime.now()))
            # Print the count of updated rows
            print(cur.rowcount)
            # Commit the updates
            db_conn.commit()
            # Close the cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db_conn is not None:
                db_conn.close()


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
                                  scope=playlistscope,
                                  cache_handler=BotCacheHandler()))

    scraped_songs = dict()
    song_count = 0

    # iterate through all the people we have
    for person in tokens.dataDict:
        # check that the person gave me the links I've asked for infinite times
        if(tokens.get_person_data(person, 'onrepeat') is not None and tokens.get_person_data(person, 'repeatrewind') is None):
            # get the On Repeat playlist data dump
            on_repeat = sp_client.playlist_items(
                tokens.get_person_data(person, 'onrepeat'), fields=None, limit=50, offset=0, market='US')
            # get the size of the On Repeat playlist
            playlist_size = on_repeat['total']
            # divde that so we can get an even number of songs per participant
            divisor = playlist_size//5
            # randomly choose some track numbers to pick from OR
            ORrands = [random.randint(0, divisor-1),
                       random.randint(divisor, divisor*2-1),
                       random.randint(divisor*2, divisor*3-1),
                       random.randint(divisor*3, divisor*4-1),
                       random.randint(divisor*4, playlist_size-1)]
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
        elif(tokens.get_person_data(person, 'onrepeat') is None and tokens.get_person_data(person, 'repeatrewind') is not None):
            # get the Repeat Rewind playlist data dump
            repeat_rewind = sp_client.playlist_items(
                tokens.get_person_data(person, 'repeatrewind'), fields=None, limit=50, offset=0, market='US')
            # get the size of the Repeat Rewind playlist
            playlist_size = repeat_rewind['total']
            # divde that so we can get an even number of songs per participant
            divisor = playlist_size//5
            # randomly choose some track numbers to pick from RR
            RRrands = [random.randint(0, divisor-1),
                       random.randint(divisor, divisor*2-1),
                       random.randint(divisor*2, divisor*3-1),
                       random.randint(divisor*3, divisor*4-1),
                       random.randint(divisor*4, playlist_size-1)]
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
        elif(tokens.get_person_data(person, 'onrepeat') is not None and tokens.get_person_data(person, 'repeatrewind') is not None):
            # get the On Repeat playlist data dump
            on_repeat = sp_client.playlist_items(
                tokens.get_person_data(person, 'onrepeat'), fields=None, limit=50, offset=0, market='US')
            # get the size of the On Repeat playlist
            playlist_size = on_repeat['total']
            # divde that so we can get an even number of songs per participant
            divisor = playlist_size//3
            # randomly choose some track numbers to pick from OR
            ORrands = [random.randint(0, divisor-1),
                       random.randint(divisor, divisor*2-1),
                       random.randint(divisor*2, playlist_size-1)]
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

    try:
        # Connect to the DB
        db_conn = psycopg2.connect(
            tokens.get_database_url(), sslmode='require')
        # Set the cursor
        cur = db_conn.cursor()
        # INSERT a record of this update
        cur.execute(
            """
            INSERT INTO tribe_blend_update (discord_id, updated_date)
            VALUES (%s, %s);
            """,
            (tokens.get_person_data('Pragosh', 'id'), datetime.now()))
        # Save the changes
        db_conn.commit()
        # Close the cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()


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
    tribeblend = sp_client.playlist_items(tokens.get_TribeBlend2_ID())
    # print results to a formatted file for viewing. (file is gitignored)
    with open('playlist_items_output', 'w') as playlist_output:
        json.dump(tribeblend, playlist_output, indent=4, sort_keys=True)
    tribeback = sp_client.playlist(tokens.get_TribeBlend2_ID())
    # print results to a formatted file for viewing. (file is gitignored)
    with open('playlist_output', 'w') as playlist_output:
        json.dump(tribeback, playlist_output, indent=4, sort_keys=True)
