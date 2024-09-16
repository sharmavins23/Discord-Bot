# ----- Discord bot designed and implemented by Curtis Maher -----
# -- Terms of Service --
# Don't copy this or I might cry

# Imports because it's cool to have other stuff
import asyncio
import discord
from discord.ext import commands
from src.spotify.spotifypassives import SpotifyPassives
from src.spotify.spotify_commands import SpotifyCommands
import src.tokens as tokens
from src.randomness import Randomness

# Initialize bot
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('Pragosh, '),
    help_command=None,
    intents=discord.Intents.all(),
)
server_token = tokens.get_application_token()


async def init_cogs():
    await bot.add_cog(Randomness(bot))
    passive_cog = SpotifyPassives(bot)
    await bot.add_cog(passive_cog)
    await passive_cog.startup()
    await bot.add_cog(SpotifyCommands(bot))


@bot.event
async def on_ready():
    bot_chat = bot.get_channel(tokens.get_bot_tchat())
    await bot_chat.send('I am Pragosh. And I am the Messiah')


# Pragosh's responses to messages
@bot.event
async def on_message(message):
    if message.author == bot.user:  # don't want to check our own messages
        return
    # instant replying to "Tatsu#8792"
    if message.author.id == tokens.get_person_data('Tatsu', 'id'):
        context = await bot.get_context(message)
        await context.message.reply("Please stop abusing your girlfriend")
    # instant WillPOG-ing
    if "POG" in message.content.upper():
        will_pog_emoji = bot.get_emoji(918323637398941716)
        await message.add_reaction(will_pog_emoji)
    # instant replying with Radical Islam
    if "RADICAL ISLAM" in message.content.upper():
        context = await bot.get_context(message)
        await context.message.reply(
            "https://media.discordapp.net/attachments/739822762062905487/1010339047614455838/image0.gif")

    await bot.process_commands(message)


# - Pragosh's direct commands -
# Help Command
@bot.command(name="help")
async def command_help(context, command=None):
    if context.message.author.bot:  # don't want to take commands from any bots
        return
    if command is None:
        help_message = 'List of current commands: \
                        \nbio \
                        \nrandomnumber \
                        \ncoinflip \
                        \nrandomcolor \
                        \ntopartists \
                        \nTBcheckpoints \
                        \nTBsong \
                        \n\nFor further help, type \'Pragosh, help `command`\''
    elif command == "bio":
        help_message = 'The bio command returns information about the currently released version of the bot'
    elif command == "randomnumber":
        help_message = 'To use the random number command, type \'Pragosh, randomnumber `starting integer` `ending integer` `count`\' \
                        \n\nNotes: \
                        \nYou can enter a single number. The output is x random numbers from 1 to 100 \
                        \nThe count of generated numbers is optional. The default is 1 (when bounded).'
    elif command == "coinflip":
        help_message = 'The coin flip command returns a randomly flipped coin featuring the immortal Queen Elizabeth'
    elif command == "randomcolor":
        help_message = 'The random color command returns a random color with the hex code'
    elif command == "topartists":
        help_message = 'The top artists command provides you with the top 5 most common artists in a playlist \
                        \nTo use this command, type: \'Pragosh, topartists `playlist link`\' \
                        \nFor example: \'Pragosh, topartists \
                        https://open.spotify.com/playlist/0fyr74e0hLjFJ3778Vw0SZ?si=0824b597bf5d4182\''
    elif command == "TBcheckpoints":
        help_message = 'The TB checkpoints command gives you a transcript of the first song for everyone in \
                        the Tribe Blend 2.0 playlist, so you can find them easier.'
    elif command == "TBsong":
        help_message = 'The TB song command gets you info about a song from TB 2.0 \
                        \nTo use this command, type \'Pragosh, TBsong `song link`\''

    await context.message.reply(help_message)


# Bot Information Command
@bot.command(name="bio")
async def bot_bio(context):
    if context.message.author.bot:  # don't want to take commands from any bots
        return

    bio_embed = discord.Embed(
        title="Hi!! I'm Pragosh.",
        description="This is all about me.",
        color=0x664616,
        url="https://github.com/18maherc/Discord-Bot"
    )
    bio_embed.add_field(
        name="Background",
        value="I am the Messiah",
        inline=False
    )
    bio_embed.add_field(
        name="Current Version",
        value="v1.6.3.1",
        inline=True
    )
    bio_embed.add_field(
        name="Release Date",
        value="December 27, 2022",
        inline=True
    )
    await context.message.reply(embed=bio_embed)


# --- Run Time ---
asyncio.run(bot.run(server_token))
asyncio.run(init_cogs())
