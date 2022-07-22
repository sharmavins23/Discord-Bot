# first idea: command to see the annotations of Tribe Blend 2.0
# second idea: command to refresh just your own chunk of 5 songs in TB2.0
# stretch of an idea: pull analytics of TB2.0
from discord.ext import commands
from . import spotifyfunctions as spfunct
from .. import localtokens as localtokens


class SpotifyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Update Tribe Blend 2.0
    @commands.command(name="updateTB2")
    async def updateTB(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        if ctx.message.author.id == localtokens.get_person_data('Curtis', 'id'):
            music_chat = self.bot.get_channel(localtokens.get_music_tchat())
            spfunct.update_TrBl2()
            await music_chat.send(f"<@&{localtokens.get_TribeBlend_role()}>, Tribe Blend 2.0 has been updated!")

    @commands.command(name="topartists")
    async def findTopArtists(self, ctx, playlistID):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        artistDict = spfunct.count_playlist_artists(str(playlistID))
        outputstring = f"The top 5 songs in {spfunct.get_playlist_name(playlistID)}:"
        for i in range(5):
            artist = artistDict[i][1]
            name = artist['artistName']
            count = artist['count']
            outputstring = outputstring+f"\n{i+1}: {name} with {count} songs"

        await ctx.message.reply(outputstring)
