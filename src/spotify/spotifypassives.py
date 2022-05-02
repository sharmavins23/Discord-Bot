import os
import discord
from discord.ext import commands, tasks
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from .. import tokens as tokens
import datetime
import random


class SpotifyPassives(commands.Cog):
    # Initialization
    def __init__(self, bot):
        # Initialize bot as self from Cog
        self.bot = bot

        # Set authorization in CC flow
        auth_manager = SpotifyClientCredentials()
        self.sp_client = spotipy.Spotify(auth_manager=auth_manager)

        # start up background tasks
        self.tribe_blend_checkup.start()

    # Convert spotify IDs to Discord role IDs
    def spotifyid_to_discordid(self, spot_id):
        # Allows us to use this dictionary as a switch-case of sorts
        return tokens.get_discordid_from_spotifyid(spot_id)

    # Pragosh's background behavior
    @tasks.loop(hours=(24*7))  # running loop every 7 days
    async def tribe_blend_checkup(self):
        # Setting a scope for CAC flow
        playlistscope = "playlist-modify-public"
        # Get CAC authorized variable
        # self.sp_auth = spotipy.Spotify(
        #    auth_manager=SpotifyOAuth(scope=playlistscope))

        trbl_update_string = f"<@&{tokens.get_TribeBlend_role}>, Tribe Blend 2.0 has been updated!"
        # Grab relevant server channels used to send messages
        music_chat = self.bot.get_channel(tokens.get_music_tchat())
        async for message in music_chat.history(limit=1000, after=(datetime.datetime.now() - datetime.timedelta(weeks=1))):
            if message.author == self.bot.user:
                if "Tribe Blend 2.0 has been updated!" in message.content:
                    return
        self.update_TrBl2()
        await music_chat.send(trbl_update_string)

    @tribe_blend_checkup.before_loop
    async def before_printer(self):
        # wait for bot to be online and ready before beginning Tribe Blend Task
        await self.bot.wait_until_ready()

    def update_TrBl2(self):
        scraped_songs = dict()
        song_count = 0

        # iterate through all the people we have
        for person in tokens.dataDict:
            # check that the person game me the links I've asked for 4 times and counting
            if(tokens.get_person_data(person, 'onrepeat') is not None and tokens.get_person_data(person, 'repeatrewind') is not None):
                # get the On Repeat playlist data dump
                on_repeat = self.sp_client.playlist_items(
                    tokens.get_person_data(person, 'onrepeat'), fields=None, limit=50, offset=0, market='US')
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
                            {f"Track{song_count}": track_info})

                # get the Repeat Rewind playlist data dump
                repeat_rewind = self.sp_client.playlist_items(
                    tokens.get_person_data(person, 'repeatrewind'), fields=None, limit=50, offset=0, market='US')
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
                    scraped_songs.update({f"Track {song_count}": track_info})

        # get our scraped songs and put them into a playlist
        self.sp_auth.playlist_replace_items(
            tokens.get_TribeBlend2_ID, (track['ID'] for track in scraped_songs))

        print(scraped_songs)
