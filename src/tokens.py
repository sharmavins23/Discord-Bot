# Pulling all environment config variables from Heroku
import os


# ===== Constants (Environment variables/Chat config) ==========================
def get_database_url():
    return os.environ['DATABASE_URL']


def get_application_token():
    return os.environ['APPLICATION_KEY']


def get_spotify_clientid():
    return os.environ['SPOTIPY_CLIENT_ID']


def get_spotify_secretid():
    return os.environ['SPOTIPY_CLIENT_SECRET']


def get_redirect_uri():
    return os.environ['SPOTIPY_REDIRECT_URI']


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
        'id': 426825197866450975,
        'role': 739842006263791688,
        'spotifyid': "asterkool",
        'onrepeat': '37i9dQZF1EprcA2aKeFg1F',
        'repeatrewind': '37i9dQZF1EpNCOTokmqvZd',
    },
    'Anand': {
        'id': 526161609572483072,
        'role': 923727693554528276,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Andy': {
        'id': 230889641073573889,
        'role': 739842129655758969,
        'spotifyid': 'totalpwnage15',
        'onrepeat': '37i9dQZF1Eph16PLUtoJ2N',
        'repeatrewind': '37i9dQZF1EpHW4SiooJKLj',
    },
    'Austin': {
        'id': 164299666714918912,
        'role': 746615079755055186,
        'spotifyid': "31s5eguzeenufwdbys5rtex4e3ay",
        'onrepeat': '37i9dQZF1EptBfPvelQzcp',
        'repeatrewind': None,
    },
    'Ben': {
        'id': 268830174416470017,
        'role': 923375385931034624,
        'spotifyid': "benjaminlight132",
        'onrepeat': '37i9dQZF1EphtOIhHQlGQm',
        'repeatrewind': '37i9dQZF1EpMoOVUkl5NHm',
    },
    'Brindle': {
        'id': 272072843917787148,
        'role': 739842298174767256,
        'spotifyid': 'ht68kx83oyis801h03x3iqa59',
        'onrepeat': '37i9dQZF1EphTASg1unLVv',
        'repeatrewind': '37i9dQZF1EpDCsWLnTtdT7',
    },
    'Curtis': {
        'id': 271732817740693505,
        'role': 739842049724907542,
        'spotifyid': "swegmaster089",
        'onrepeat': '37i9dQZF1EpmZMSJIctDsD',
        'repeatrewind': '37i9dQZF1EpMg8wKIo1afC',
    },
    'Ed': {
        'id': 212318224342056961,
        'role': 938256001847656498,
        'spotifyid': '31dnmpsmzxlx4nmh3hpwu625awfa',
        'onrepeat': '37i9dQZF1EpwTREFiceW5T',
        'repeatrewind': '37i9dQZF1EpFkTPe7Nl0Qv',
    },
    'Finn': {
        'id': 267520125710630913,
        'role': 873272343592591420,
        'spotifyid': 'freelancebean02',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Joey': {
        'id': 402289709407141888,
        'role': 926958113171603456,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Kennedy': {
        'id': 329813627307687936,
        'role': 742208791004708984,
        'spotifyid': '22x6phuiclyuuuqjalypbt74a',
        'onrepeat': '37i9dQZF1EpiELg1ftzNgh',
        'repeatrewind': '37i9dQZF1EpJ5FSmj5o2Mr',
    },
    'Kevin': {
        'id': 323888373662220298,
        'role': 923375312094519338,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Logan': {
        'id': 328330822962905088,
        'role': 740545339622293604,
        'spotifyid': 'q3tg252wqc5ntxe2fagbdtchu',
        'onrepeat': '37i9dQZF1EpoNXfvyxK7HG',
        'repeatrewind': '37i9dQZF1EpHIChtwK4I34',
    },
    'Mike': {
        'id': 218064586929209345,
        'role': 739842089579184269,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Nick': {
        'id': 902272488103366677,
        'role': 739842393481674783,
        'spotifyid': "fitterminator",
        'onrepeat': "37i9dQZF1EpyPACl8m2SO3",
        'repeatrewind': '37i9dQZF1EpCxNRIBP44gj',
    },
    'Gick': {
        'id': 490082119297662977,
        'role': 887103144172068925,
        'spotifyid': "7a9uyyfrf5m61tft6anmx3csp",
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Payton': {
        'id': 399258844452356107,
        'role': 739842348980109402,
        'spotifyid': "nia8wdzes92kopprtw6mlj4xz",
        'onrepeat': '37i9dQZF1EpgD6ACJX1Y4k',
        'repeatrewind': '37i9dQZF1EpUunxyPDyBAK',
    },
    'Sam': {
        'id': 271089783323885579,
        'role': 992875363673837609,
        'spotifyid': '315wrb4upjcifhw3pqfykwwipgi4',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Tatsu': {
        'id': 172002275412279296,
        'role': 748016599038165053,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Vineeth': {
        'id': 236964881213947914,
        'role': 739841745508106322,
        'spotifyid': "v9iqkldb8yaxvvifjqwhzijxx",
        'onrepeat': "37i9dQZF1EpuLO8qSlx7VC",
        'repeatrewind': "37i9dQZF1EpGWwKBPqIySc"
    },
    'Will': {
        'id': 122489106818138113,
        'role': 918702896135151638,
        'spotifyid': None,
        'onrepeat': None,
        'repeatrewind': None,
    },
    'Pragosh': {
        'id': 796485108588216380,
        'role': 883740669020106812,
        'spotifyid': 'mlgcongress',
        'onrepeat': None,
        'repeatrewind': None,
    },
    'AlphaPragosh': {
        'id': 942940638234681414,
        'role': 883740669020106812,
        'spotifyid': 'mlgcongress',
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
