# Pulling all environment config variables from Heroku
import os


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


def get_Adam_role():
    return int(os.environ['ADAM_ROLE'])


def get_Anand_role():
    return int(os.environ['ANAND_ROLE'])


def get_Andrew_role():
    return int(os.environ['ANDREW_ROLE'])


def get_Andy_role():
    return int(os.environ['ANDY_ROLE'])


def get_Austin_role():
    return int(os.environ['AUSTIN_ROLE'])


def get_Ben_role():
    return int(os.environ['BEN_ROLE'])


def get_Brindle_role():
    return int(os.environ['BRINDLE_ROLE'])


def get_Curtbot_role():
    return int(os.environ['CURTBOT_ROLE'])


def get_Curtis_role():
    return int(os.environ['CURTIS_ROLE'])


def get_Ed_role():
    return int(os.environ['ED_ROLE'])


def get_Finn_role():
    return int(os.environ['FINN_ROLE'])


def get_Joey_role():
    return int(os.environ['JOEY_ROLE'])


def get_Kennedy_role():
    return int(os.environ['KENNEDY_ROLE'])


def get_Kevin_role():
    return int(os.environ['KEVIN_ROLE'])


def get_Logan_role():
    return int(os.environ['LOGAN_ROLE'])


def get_Mike_role():
    return int(os.environ['MIKE_ROLE'])


def get_Nick_role():
    return int(os.environ['NICK_ROLE'])


def get_NickG_role():
    return int(os.environ['NICKG_ROLE'])


def get_Payton_role():
    return int(os.environ['PAYTON_ROLE'])


def get_TribeBlend_role():
    return int(os.environ['TRIBEBLEND_ROLE'])


def get_Vineeth_role():
    return int(os.environ['VINEETH_ROLE'])


def get_Will_role():
    return int(os.environ['WILL_ROLE'])


def get_TribeBlend1_ID():
    return '4zJqkYjPGRSv2TLvISLp7x'


def get_TribeBlend2_ID():
    return '2JML26sLyhDe3LWjJMjMl5'
