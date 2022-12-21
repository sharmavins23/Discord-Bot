import random
from discord.ext import commands
import discord


class Randomness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Random color generator command
    @commands.command(name="randomnumber")
    async def rand_num(self, ctx, lower_bound=None, upper_bound=None, count=0):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        # Check if we were given arguments
        if lower_bound is None:
            await ctx.message.reply("Give me a number, numb nuts.")
        # Check if we there's a negative lower bound
        elif int(lower_bound) < 0:
            await ctx.message.reply("I'm a positive guy. I don't do negatives.")
        else:
            lower_bound = int(lower_bound)
            # Check if we're getting a bunch of random numbers
            if upper_bound is None:
                # Limit the number of random numbers
                count = min(lower_bound, 100)
                # Setup our output string
                random_numbers_str = ''
                # Iterate through making the numbers and output string
                while count > 0:
                    # Get a random number, bounded within 1 to 100
                    number = random.randint(1, 100)
                    # Add it to the string
                    random_numbers_str = random_numbers_str + \
                        str(number) + ', '
                    # Decrement for next loop
                    count -= 1
                # Get rid of trailing characters in string
                random_numbers_str = random_numbers_str[:-2]
                # Send reply output in Discord
                await ctx.message.reply(f"Your random number(s): {random_numbers_str}")
            else:
                upper_bound = int(upper_bound)
                # Check if the bounds are the same number
                if upper_bound == lower_bound:
                    await ctx.message.reply("Are you dumb or are you trolling??")
                # Check is lower bound is higher
                elif upper_bound < lower_bound:
                    await ctx.message.reply("Your bounds are out of whack, son.")
                else:
                    # Check if upper bound is absurdly high
                    if upper_bound > 1_000_000:
                        await ctx.message.reply("I only go to 1 million bc I'm smol brain.")
                    else:
                        # Setup our output string
                        random_numbers_str = ''
                        # Limit the number of random numbers
                        count = min(count, 100)
                        # Check if count is a negative number or default 0
                        if count <= 0:
                            # Set count to a single number
                            count = 1
                        # Iterate through making the numbers and output string
                        while count > 0:
                            # Get a random number, bounded within given bounds
                            number = random.randint(lower_bound, upper_bound)
                            # Add it to the string
                            random_numbers_str = random_numbers_str + \
                                str(number) + ', '
                            # Decrement for next loop
                            count -= 1
                        # Get rid of trailing characters in string
                        random_numbers_str = random_numbers_str[:-2]
                        # Send reply output in Discord
                        await ctx.message.reply(f"Your random number(s): {random_numbers_str}")
        return

    # Coin Flip Command
    @commands.command(name="coinflip")
    async def coin_flip(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        # Get a random number to represent heads or tails
        flip = random.randint(1, 2)
        # Check if it is heads
        if flip == 1:
            await ctx.message.reply(
                file=discord.File('./img/FlippedHeads.png'))
        # Otherwise it is tails
        else:
            await ctx.message.reply(
                file=discord.File('./img/FlippedTails.png'))

    # Random color command
    @commands.command(name="randomcolor")
    async def rand_color(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        # Generate a random color's R, G, and B values
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Convert R, G, and B values to hexadecimal value strings and pad 0s
        r_hex = str(hex(r)).replace('0x', '').zfill(2)
        g_hex = str(hex(g)).replace('0x', '').zfill(2)
        b_hex = str(hex(b)).replace('0x', '').zfill(2)

        # Concatenate the hex value strings together
        color_hex = (r_hex + g_hex + b_hex).upper()

        # Create an embed with the color as our RGB color
        color_embed = discord.Embed(
            color=discord.Color.from_rgb(r, g, b),
        )
        # Change the image of the embed
        color_embed.set_image(
            url=f"https://dummyimage.com/420x69/{color_hex}/&text=%23{color_hex}")

        await ctx.message.reply(embed=color_embed)
