# Terms of Service:
# Don't copy this or I might cry

# Imports because it's cool to have other stuff
from server_token import getToken
import discord

# Client - this is where the bot comes outta the womb
client = discord.Client()

# Variables because calling stuff smaller stuff makes me a happy chappy
server_token = getToken()
gen_chat = client.get_channel(739822762062905487)
music_chat = client.get_channel(744697370469728347)
meme_chat = client.get_channel(739912364119556167)
tech_chat = client.get_channel(752552118577266709)
hw_chat = client.get_channel(805806903656841237)
pics_chat = client.get_channel(742423632524869732)
spam_chat = client.get_channel(743540423586349196)
scary_chat = client.get_channel(833023208902492200)
bot_chat = client.get_channel(883740406469234718)
gen_vchat = client.get_channel(739822762062905488)

# Work Time


# Run Time
client.run(server_token)
