# first idea: command to see the annotations of Tribe Blend 2.0
# second idea: command to refresh just your own chunk of 5 songs in TB2.0
# stretch of an idea: pull analytics of TB2.0
from discord.ext import commands
from .spotifyfunctions import update_TrBl2
from .. import tokens as tokens


class SpotifyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Random color generator command
    @commands.command(name="updateTB2")
    async def updateTB(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        if ctx.message.author == 271732817740693505:
            music_chat = self.bot.get_channel(tokens.get_music_tchat())
            update_TrBl2()
            await music_chat.send(f"<@&{tokens.get_TribeBlend_role()}>, Tribe Blend 2.0 has been updated!")
