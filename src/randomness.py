import random
import discord
from discord.ext import commands


class Randomness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Random color generator command

    @commands.command(name="randomcolor")
    async def rand_color(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return
        color_int = random.randint(0, pow(2, 24))
        color_hex = hex(color_int)
        # need to figure how I want to get the R G and B from the int or the hex

    # Coin Flip Command

    @commands.command(name="coinflip")
    async def coin_flip(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return
        flip = random.randint(1, 2)
        if flip == 1:
            await ctx.message.reply('https://cdn.discordapp.com/attachments/883740406469234718/927397534568165436/FlippedHeads.png')
        else:
            await ctx.message.reply('https://cdn.discordapp.com/attachments/883740406469234718/927397541237129216/FlippedTails.png')
