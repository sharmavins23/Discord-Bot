# ----- Discord bot designed and implemented by Curtis Maher -----
# -- Terms of Service --
# Don't copy this or I might cry

# Imports because it's cool to have other stuff
import os
import discord
from discord.ext import commands
import spotipy
from src.spotify.spotifypassives import SpotifyPassives
import src.tokens as tokens
from src.randomness import Randomness

# Initialize bot
client = commands.Bot(command_prefix=commands.when_mentioned_or(
    'Pragosh, '), help_command=None)
client.add_cog(Randomness(client))
client.add_cog(SpotifyPassives(client))

# Variables because calling stuff smaller stuff makes me a happy chappy
server_token = tokens.get_application_token()


# --- Work Time ---
# Pragosh's startup sequence
@client.event
async def on_ready():
    bot_chat = client.get_channel(tokens.get_bot_tchat())
    await bot_chat.send('I am Pragosh. And I am the Messiah')


# Pragosh's responses to messages
@client.event
async def on_message(message):
    if message.author == client.user:  # don't want to check our own messages
        return
    if message.author.id == 172002275412279296:  # instant replying to "Tatsu#8792"
        context = await client.get_context(message)
        await context.message.reply("Please stop abusing your girlfriend")
    elif "POG" in message.content.upper():  # instant reacting to messages with pog
        will_pog_emoji = client.get_emoji(918323637398941716)
        await message.add_reaction(will_pog_emoji)

    await client.process_commands(message)


# - Pragosh's direct commands -
# Help Command
@client.command(name="help")
async def command_help(context, command=None):
    if context.message.author.bot:  # don't want to take commands from any bots
        return
    if command == None:
        help_message = 'List of current commands: \nbio \nrandomnumber \ncoinflip \n\nFor further help, type \'Pragosh, help `command`\''
    elif command == "bio":
        help_message = 'The bio command returns information about the currently released version of the bot'
    elif command == "randomnumber":
        help_message = 'To use the random number function, type \'Pragosh, randomnumber `starting integer` `ending integer` `count`\'\n\nNote: The count of generated numbers is optional. The default is 1'
    elif command == "coinflip":
        help_message = 'The coin flip command returns a randomly flipped coin featuring the immortal Queen Elizabeth'

    await context.message.reply(help_message)


# Bot Information Command
@client.command(name="bio")
async def bot_bio(context):
    if context.message.author.bot:  # don't want to take commands from any bots
        return
    bio_embed = discord.Embed(
        title="Hi!! I'm Pragosh.", description="This is all about me.", color=0x664616, url="https://github.com/18maherc/Discord-Bot")
    bio_embed.add_field(name="Background",
                        value="I am the Messiah", inline=False)
    bio_embed.add_field(name="Current Version",
                        value="v1.4.2.2", inline=True)
    bio_embed.add_field(name="Release Date",
                        value="February 16, 2022", inline=True)
    await context.message.reply(embed=bio_embed)


# --- Run Time ---
client.run(server_token)
