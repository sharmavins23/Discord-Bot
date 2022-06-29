# first idea: command to see the annotations of Tribe Blend 2.0
# second idea: command to refresh just your own chunk of 5 songs in TB2.0
# stretch of an idea: pull analytics of TB2.0
from discord.ext import commands
from .spotifyfunctions import update_TrBl2
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
            update_TrBl2()
            await music_chat.send(f"<@&{localtokens.get_TribeBlend_role()}>, Tribe Blend 2.0 has been updated!")
