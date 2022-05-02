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


def get_TribeBlend_role():
    return 918982886886096957


def get_TribeBlend1_ID():
    return '4zJqkYjPGRSv2TLvISLp7x'


def get_TribeBlend2_ID():
    return '2JML26sLyhDe3LWjJMjMl5'


# ===== Person-specific data ===================================================


dataDict = {
    'Adam': {
        'role': 739842006263791688,
        'spotifyid': "asterkool",
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Anand': {
        'role': 923727693554528276,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Andrew': {
        'role': 744023449613107203,
        'spotifyid': '21mujp7bog4xtib3zfj4hwqmi',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Andy': {
        'role': 739842129655758969,
        'spotifyid': 'totalpwnage15',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Austin': {
        'role': 746615079755055186,
        'spotifyid': "31s5eguzeenufwdbys5rtex4e3ay",
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Ben': {
        'role': 923375385931034624,
        'spotifyid': "benjaminlight132",
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Brindle': {
        'role': 739842298174767256,
        'spotifyid': 'ht68kx83oyis801h03x3iqa59',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Curtbot': {
        'role': 883740669020106812,
        'spotifyid': 'mlgcongress',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Curtis': {
        'role': 739842049724907542,
        'spotifyid': "swegmaster089",
        'onrepeat': '37i9dQZF1EpmZMSJIctDsD',
        'repeatrewind': '37i9dQZF1EpMg8wKIo1afC',
    },
    'Ed': {
        'role': 938256001847656498,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Finn': {
        'role': 873272343592591420,
        'spotifyid': 'freelancebean02',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Joey': {
        'role': 926958113171603456,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Kennedy': {
        'role': 742208791004708984,
        'spotifyid': '22x6phuiclyuuuqjalypbt74a',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Kevin': {
        'role': 923375312094519338,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Logan': {
        'role': 740545339622293604,
        'spotifyid': 'q3tg252wqc5ntxe2fagbdtchu',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Mike': {
        'role': 739842089579184269,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Nick': {
        'role': 739842393481674783,
        'spotifyid': "fitterminator",
        'onrepeat': "37i9dQZF1EpyPACl8m2SO3",
        'repeatrewind': '37i9dQZF1EpCxNRIBP44gj',
    },
    'Gick': {
        'role': 887103144172068925,
        'spotifyid': "7a9uyyfrf5m61tft6anmx3csp",
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Payton': {
        'role': 739842348980109402,
        'spotifyid': "nia8wdzes92kopprtw6mlj4xz",
        'onrepeat': '37i9dQZF1EpgD6ACJX1Y4k',
        'repeatrewind': '37i9dQZF1EpUunxyPDyBAK',
    },
    'Vins': {
        'role': 739841745508106322,  # Use Vins instead reee
        'spotifyid': "v9iqkldb8yaxvvifjqwhzijxx",
        'onrepeat': "37i9dQZF1EpuLO8qSlx7VC",
        'repeatrewind': "37i9dQZF1EpGWwKBPqIySc"
    },
    'Will': {
        'role': 918702896135151638,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    }
}


# Get some data from the dataDict
def get_person_data(name: str, thing: str):
    """ Gets whatever you need for someone in the server

    Args:
        - name: name of the user, e.g. 'Pragosh'
        - thing: 'role', 'spotifyid', 'onrepeat', or 'repeatrewind'

    Returns:
        - str: string of requested ID or int value of Role ID
    """
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
        name = person
        spotifyid = person['spotifyid']
        if spotifyid == spot_id:
            return name


def get_name_from_discordid(discid):
    for person in dataDict:
        name = person
        discordid = person['role']
        if discordid == discid:
            return name
