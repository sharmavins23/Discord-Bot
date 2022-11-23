# first idea: command to see the annotations of Tribe Blend 2.0
# second idea: command to refresh just your own chunk of 5 songs in TB2.0
# stretch of an idea: pull analytics of TB2.0
from discord.ext import commands
from . import spotifyfunctions as spfunct
from .. import tokens as tokens


class SpotifyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Update Tribe Blend 2.0
    @commands.command(name="updateTB2")
    async def update_TB(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        # Only the creator of Pragosh has the authority for this command
        if ctx.message.author.id == tokens.get_person_data('Curtis', 'id'):
            bot_chat = self.bot.get_channel(tokens.get_bot_tchat())
            # Update the playlist
            spfunct.update_TrBl2()
            # Make a record of this update
            await bot_chat.send("Tribe Blend 2.0 has been updated!")

    @commands.command(name="topartists")
    async def find_top_artists(self, ctx, playlistID):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        # Get our artist dictionary
        artistDict = spfunct.count_playlist_artists(str(playlistID))
        # Begin creating our output string
        outputstring = f"The top 5 songs in {spfunct.get_playlist_name(playlistID)}:"
        # Let's check out the top 5 artists
        for i in range(5):
            artist = artistDict[i][1]
            name = artist['artistName']
            count = artist['count']
            # Add our contents to the output string
            outputstring = outputstring+f"\n{i+1}: {name} with {count} songs"
        # Send the output string
        await ctx.message.reply(outputstring)

    @commands.command(name="TBcheckpoints")
    async def get_TB_chkp(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        await ctx.message.reply(spfunct.get_checkpoints())
