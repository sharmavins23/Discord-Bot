from discord.ext import commands
import discord
import math


class BettingOdds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Betting odds compute command
    @commands.command(name="bettingodds")
    async def bettingodds(self, ctx, odds, dollars=100):
        if ctx.message.author.bot:  # Azimov's laws of roboethics
            return

        # Parse the odds string into a number
        try:
            odds = int(odds)
        except ValueError:
            await ctx.message.reply("Those odds are not a number, dummy.")
            return

        # Get the sign of the value and handle the formula accordingly
        if odds > 0:
            fractionalOdds = (odds / 100) + 1
        elif odds < 0:
            fractionalOdds = (-100 / odds) + 1
        else:
            await ctx.message.reply("You can't bet on a 0% chance of winning, dummy.")
            return

        # Compute the bet amount
        betAmount = dollars * fractionalOdds

        await ctx.message.reply(f"For a bet of ${dollars}, if you win you'll make ${betAmount} total.")
        return
