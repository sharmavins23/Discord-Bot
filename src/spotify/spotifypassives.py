import os
import discord
from discord.ext import commands, tasks
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from .. import tokens as tokens
import datetime


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
        trbl_update_string = f"<@&{tokens.get_TribeBlend_role}>, Tribe Blend 2.0 has been updated!"
        # Grab relevant server channels used to send messages
        music_chat = self.bot.get_channel(tokens.get_music_tchat())
        async for message in music_chat.history(limit=1000, after=(datetime.datetime.now() - datetime.timedelta(weeks=1))):
            if message.author == self.bot.user:
                if "Tribe Blend 2.0 has been updated!" in message.content:
                    return
                else:
                    update_TrBl2()
                    await music_chat.send(trbl_update_string)

        # letting music channel know that the process is beginning
        # await music_chat.send('Checking Spotify...')

        # Setting a scope for CAC flow
        # playlistscope = "playlist-read-collaborative"
        # Get CAC authorized variable
        # sp_auth = spotipy.Spotify(
        #    auth_manager=SpotifyOAuth(scope=playlistscope))

        # Get track information for Tribe Blend playlist via playlistID
        tribe_blend = self.sp_client.playlist_tracks(
            '4zJqkYjPGRSv2TLvISLp7x', fields=None, limit=100, offset=0, market='US')

        # Manipulatable 2D list for necessary playlist info
        blend_list = [['#'], ['Track Name'], ['Added By'], ['Added At']]
        # Loop through entire playlist to look at each item's information
        for idx, item in enumerate(tribe_blend['items']):
            # Setting info of when track was added to playlist
            added_at = item['added_at']
            # Changing the added info into a datetime format
            added_datetime = datetime.datetime.strptime(
                added_at, '%Y-%m-%dT%H:%M:%SZ')
            # Changing to EST
            added_datetime = added_datetime - datetime.timedelta(hours=7)
            # Setting an old date threshold for tracks added to playlist
            old_date = datetime.datetime.now() - datetime.timedelta(weeks=4)

            # If an added track is too old...
            if added_datetime < old_date:
                # Counting our number of tracks in playlist and adding to the list
                blend_list[0].append(idx+1)
                # Getting current track information
                track = item['track']
                # Adding the track name to our list
                blend_list[1].append(track['name'])
                # Getting information of user that added the track
                added_by = item['added_by']
                # Changing user's ID to a discord role ID and adding to list
                blend_list[2].append(
                    self.spotifyid_to_discordid(added_by['id']))
                # Adding modified added info to list
                blend_list[3].append(added_datetime)

        # Creating a list to track users that we have already messaged
        ping_list = []
        # Looping through playlist info 2D list
        for item in enumerate(blend_list[2]):
            # Skipping over header entry
            if item[1] == 'Added By':
                continue
            # Check that we have not already pinged this ID item
            if item[1] not in (ping_list):
                await music_chat.send(
                    '<@&'+str(item[1])+'> You have stuff in Tribe Blend that is over 4 weeks old!!')
            # Add this ID item to the list of users already messaged
            ping_list.append(item[1])

    @tribe_blend_checkup.before_loop
    async def before_printer(self):
        # wait for bot to be online and ready before beginning Tribe Blend Task
        await self.bot.wait_until_ready()
