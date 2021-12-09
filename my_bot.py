# Discord bot designed and implemented by Curtis Maher
# Terms of Service:
# Don't copy this or I might cry

# Imports because it's cool to have other stuff
from server_token import get_server_token
import channel_tokens
import discord

# Client - this is where the bot comes outta the womb
client = discord.Client()


# Variables because calling stuff smaller stuff makes me a happy chappy
server_token = get_server_token()
gen_chat = client.get_channel(channel_tokens.get_gen_tchat())
music_chat = client.get_channel(channel_tokens.get_music_tchat())
meme_chat = client.get_channel(channel_tokens.get_meme_tchat())
tech_chat = client.get_channel(channel_tokens.get_tech_tchat())
hw_chat = client.get_channel(channel_tokens.get_hw_tchat())
pics_chat = client.get_channel(channel_tokens.get_pics_tchat())
spam_chat = client.get_channel(channel_tokens.get_spam_tchat())
scary_chat = client.get_channel(channel_tokens.get_scary_tchat())

gen_vchat = client.get_channel(channel_tokens.get_gen_vchat())


# Work Time
# Pragosh's startup sequence
@client.event
async def on_connect():
    bot_chat = client.get_channel(channel_tokens.get_bot_tchat())
    await bot_chat.send('I am Pragosh. And I am the Messiah')


# Pragosh's biography. Only sent when asked
@client.event
async def on_message(message):
    if message.content == 'Pragosh, who are you?':
        bio_embed = discord.Embed(
            title="Hi!! I'm Pragosh.", description="This is all about me.", color=0x664616, url="https://github.com/18maherc/Discord-Bot")
        bio_embed.add_field(name="Background",
                            value="I am the Messiah", inline=False)
        bio_embed.add_field(name="Current Version",
                            value="v1.1.0", inline=True)
        bio_embed.add_field(name="Release Date",
                            value="December 08, 2021", inline=True)
        await message.reply(embed=bio_embed)
    elif "POG" in message.content.upper():
        will_pog_emoji = client.get_emoji(918323637398941716)
        await message.add_reaction(will_pog_emoji)


# Run Time
client.run(server_token)
