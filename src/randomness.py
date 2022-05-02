import random
from discord.ext import commands


class Randomness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Random color generator command
    @commands.command(name="randomnumber")
    async def rand_num(self, ctx, lower_bound=0, upper_bound=0, count=0):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        # Bounds checks on random numbers
        arbitrarilyHighNumber = 100_000
        if upper_bound > arbitrarilyHighNumber:
            await ctx.message.reply(
                f"The upper bound is too high. Please stop being like Ed and choose a reasonable number."
            )
            return

        random_numbers_str = ''
        if count == 0:
            count = 1
        while count > 0:
            number = random.randint(lower_bound, upper_bound)
            random_numbers_str = random_numbers_str + str(number) + ', '
            count -= 1
        random_numbers_str = random_numbers_str[:-2]
        await ctx.message.reply("Your random number(s): " + random_numbers_str)

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

    # Random color command
    @commands.command(name="randomcolor")
    async def rand_color(self, ctx):
        if ctx.message.author.bot:  # don't take no commands from no robo-bots
            return

        # Generate a random color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Convert to hexadecimal value strings and pad 0s
        r_hex = str(hex(r)).replace('0x', '').zfill(2)
        g_hex = str(hex(g)).replace('0x', '').zfill(2)
        b_hex = str(hex(b)).replace('0x', '').zfill(2)

        # Concatenate the hex values together
        color_hex = '#' + r_hex + g_hex + b_hex

        await ctx.message.reply(
            f"View your random color here: https://color.aurlien.net/{color_hex}"
        )
