# Pulling all environment config variables from Heroku
import os


# ===== Constants (Environment variables/Chat config) ==========================


def get_application_token():
    return os.environ['APPLICATION_KEY']


def get_spotify_clientid():
    return os.environ['SPOTIFY_CLIENT']


def get_spotify_secretid():
    return os.environ['SPOTIFY_SECRET']


def get_redirect_uri():
    return os.environ['REDIRECT_URI']


def get_gen_tchat():
    return int(os.environ['GEN_TCHAT'])


def get_music_tchat():
    return int(os.environ['MUSIC_TCHAT'])


def get_meme_tchat():
    return int(os.environ['MEME_TCHAT'])


def get_tech_tchat():
    return int(os.environ['TECH_TCHAT'])


def get_hw_tchat():
    return int(os.environ['HW_TCHAT'])


def get_pics_tchat():
    return int(os.environ['PICS_TCHAT'])


def get_spam_tchat():
    return int(os.environ['SPAM_TCHAT'])


def get_scary_tchat():
    return int(os.environ['SCARY_TCHAT'])


def get_bot_tchat():
    return int(os.environ['BOT_TCHAT'])


def get_gen_vchat():
    return int(os.environ['GEN_VCHAT'])


def get_TribeBlend1_ID():
    return '4zJqkYjPGRSv2TLvISLp7x'


def get_TribeBlend2_ID():
    return '2JML26sLyhDe3LWjJMjMl5'


# ===== Person-specific data ===================================================


dataDict = {
    'Adam': {
        'role': int(os.environ['ADAM_ROLE']),
        'spotifyid': "asterkool",
    },
    'Anand': {
        'role': int(os.environ['ANAND_ROLE']),
        'spotifyid': None,
    },
    'Andrew': {
        'role': int(os.environ['ANDREW_ROLE']),
    },
    'Andy': {
        'role': int(os.environ['ANDY_ROLE']),
        'spotifyid': 'totalpwnage15',
    },
    'Austin': {
        'role': int(os.environ['AUSTIN_ROLE']),
        'spotifyid': "31s5eguzeenufwdbys5rtex4e3ay",
    },
    'Ben': {
        'role': int(os.environ['BEN_ROLE']),
        'spotifyid': "benjaminlight132",
    },
    'Brindle': {
        'role': int(os.environ['BRINDLE_ROLE']),
        'spotifyid': 'ht68kx83oyis801h03x3iqa59',
    },
    'Curtbot': {
        'role': int(os.environ['CURTBOT_ROLE']),
    },
    'Curtis': {
        'role': int(os.environ['CURTIS_ROLE']),
        'spotifyid': "swegmaster089",
    },
    'Ed': {
        'role': int(os.environ['ED_ROLE']),
    },
    'Finn': {
        'role': int(os.environ['FINN_ROLE']),
    },
    'Joey': {
        'role': int(os.environ['JOEY_ROLE']),
    },
    'Kennedy': {
        'role': int(os.environ['KENNEDY_ROLE']),
    },
    'Kevin': {
        'role': int(os.environ['KEVIN_ROLE']),
    },
    'Logan': {
        'role': int(os.environ['LOGAN_ROLE']),
        'spotifyid': 'q3tg252wqc5ntxe2fagbdtchu',
    },
    'Mike': {
        'role': int(os.environ['MIKE_ROLE']),

    },
    'Nick': {
        'role': int(os.environ['NICK_ROLE']),
        'spotifyid': "fitterminator",
        'onrepeat': "https://open.spotify.com/playlist/37i9dQZF1EpyPACl8m2SO3?si=x9uSl59LQMOB1HllMnu1bg",
        'repeatrewind': 'https://open.spotify.com/playlist/37i9dQZF1EpCxNRIBP44gj?si=-Vr5hmKFRvyOXDXpMHQ0gQ',
    },
    'Gick': {
        'role': int(os.environ['NICKG_ROLE']),
        'spotifyid': "7a9uyyfrf5m61tft6anmx3csp",
    },
    'Payton': {
        'role': int(os.environ['PAYTON_ROLE']),
        'spotifyid': "nia8wdzes92kopprtw6mlj4xz",
    },
    'Vins': {
        'role': int(os.environ['VINEETH_ROLE']),  # Use Vins instead reee
        'spotifyid': "v9iqkldb8yaxvvifjqwhzijxx",
        'onrepeat': "https://open.spotify.com/playlist/37i9dQZF1EpuLO8qSlx7VC?si=345dd2bf74a54ddc",
        'repeatrewind': "https://open.spotify.com/playlist/37i9dQZF1EpGWwKBPqIySc?si=2dcc8959a521459a"
    },
    'Will': {
        'role': int(os.environ['WILL_ROLE']),
    }

}


# Get some data from the dataDict
# - Acceptable "things" are:
#  - 'role'
#  - 'spotifyid'
#  - 'onrepeat'
#  - 'repeatrewind'
def get_person_data(name, thing):
    return dataDict[name][thing]


# Given a spotify ID, get the corresponding role
def get_discordid_from_spotifyid(spot_id):
    for person in dataDict:
        role = person['role']
        spotifyid = person['spotifyid']

        if spotifyid == spot_id:
            return role


# Given a spotify ID, get the corresponding name
def get_name_from_spotifyid(spot_id):
    for person in dataDict:
        name = person['role']
        spotifyid = person['spotifyid']

        if spotifyid == spot_id:
            return name


def get_TribeBlend_role():
    return int(os.environ['TRIBEBLEND_ROLE'])
