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
<<<<<<< HEAD
        color_int = random.randint(0, pow(2, 24))
        color_hex = hex(color_int)
        # need to figure how I want to get the R G and B from the int or the hex
=======

        random_numbers_str = ''
        if count == 0:
            count = 1
        while count > 0:
            number = random.randint(lower_bound, upper_bound)
            random_numbers_str = random_numbers_str + str(number) + ', '
            count -= 1
        random_numbers_str = random_numbers_str[:-2]
        await ctx.message.reply("Your random number(s): " + random_numbers_str)
>>>>>>> 23e5bb2015c60d3906e61bd6615b1766497b208b

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
