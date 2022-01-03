import discord
from discord.ext import commands
import spotipy
import spotify_tokens


class SpotifyPassives(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Pragosh's background behavior
    # @tasks.loop(seconds=1.0)
    # async def tribe_blend_checkup():
    #    bot_chat = client.get_channel(channel_tokens.get_bot_tchat())
    #    await bot_chat.send('lol')
