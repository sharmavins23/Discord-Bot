import os
import discord
from discord.ext import commands, tasks
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from .. import tokens as tokens
import datetime
import random
import spotifyfunctions as Sfunct


class SpotifyPassives(commands.Cog):
    # Initialization
    def __init__(self, bot):
        # Initialize bot as self from Cog
        self.bot = bot

        # start up background tasks
        self.tribe_blend_checkup.start()

    # Convert spotify IDs to Discord role IDs
    def spotifyid_to_discordid(self, spot_id):
        # Allows us to use this dictionary as a switch-case of sorts
        return tokens.get_discordid_from_spotifyid(spot_id)

    # Pragosh's background behavior
    @tasks.loop(hours=(24*7))  # running loop every 7 days
    async def tribe_blend_checkup(self):
        # Grab relevant server channels used to send messages
        music_chat = self.bot.get_channel(tokens.get_music_tchat())
        trbl_update_string = f"<@&{tokens.get_TribeBlend_role()}>, Tribe Blend 2.0 has been updated!"

        for message in music_chat.history(limit=100, after=(datetime.datetime.now() - datetime.timedelta(weeks=1))):
            print('We in the juice')
        if message.author == self.bot.user:
            if "Tribe Blend 2.0 has been updated!" in message.content:
                print('Time to exit')
                return
        Sfunct.tribe_blend2()
        await music_chat.send(trbl_update_string)

    @tribe_blend_checkup.before_loop
    async def before_printer(self):
        # wait for bot to be online and ready before beginning Tribe Blend Task
        await self.bot.wait_until_ready()
