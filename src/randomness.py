import random
from discord.ext import commands
import discord


class Randomness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Random color generator command
    @commands.command(name="randomnumber")
    async def rand_num(self, ctx, lower_bound=0, upper_bound=0, count=0):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        lower_bound = int(lower_bound)
        upper_bound = int(upper_bound)

        if lower_bound <= 0:
            await ctx.message.reply("I'm a positive guy. I don't do negatives.")
        else:
            if upper_bound == lower_bound:
                await ctx.message.reply("Are you dumb or are you trolling??")
            elif upper_bound < lower_bound:
                await ctx.message.reply("Your bounds are out of whack, son.")
            else:
                if upper_bound > 1_000_000:
                    await ctx.message.reply("I only go to 1 million bc I'm smol brain.")
                else:
                    random_numbers_str = ''
                    if count == 0:
                        count = 1
                    while count > 0:
                        number = random.randint(lower_bound, upper_bound)
                        random_numbers_str = random_numbers_str + \
                            str(number) + ', '
                        count -= 1
                    random_numbers_str = random_numbers_str[:-2]
                    await ctx.message.reply(f"Your random number(s): {random_numbers_str}")
        return

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
        if ctx.message.author.bot:  # don't want to take commands from any bots
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
        color_hex = (r_hex + g_hex + b_hex).upper()

        color_embed = discord.Embed(
            color=discord.Color.from_rgb(r, g, b),
        )
        color_embed.set_image(
            url=f"https://dummyimage.com/420x69/{color_hex}/&text=%23{color_hex}")

        await ctx.message.reply(embed=color_embed)
