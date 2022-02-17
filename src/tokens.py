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
    return os.environ['GEN_TCHAT']


def get_music_tchat():
    return os.environ['MUSIC_TCHAT']


def get_meme_tchat():
    return os.environ['MEME_TCHAT']


def get_tech_tchat():
    return os.environ['TECH_TCHAT']


def get_hw_tchat():
    return os.environ['HW_TCHAT']


def get_pics_tchat():
    return os.environ['PICS_TCHAT']


def get_spam_tchat():
    return os.environ['SPAM_TCHAT']


def get_scary_tchat():
    return os.environ['SCARY_TCHAT']


def get_bot_tchat():
    bot_tchat = os.environ['BOT_TCHAT']
    if type(bot_tchat) == str:
        bot_tchat = int(bot_tchat)
    elif type(bot_tchat) == int:
        pass  # Nothing to do here!
    else:
        raise ValueError(f"We got some weird type: {type(bot_tchat)}")

    return bot_tchat


def get_gen_vchat():
    return os.environ['GEN_VCHAT']


def get_Adam_role():
    return os.environ['ADAM_ROLE']


def get_Anand_role():
    return os.environ['ANAND_ROLE']


def get_Andrew_role():
    return os.environ['ANDREW_ROLE']


def get_Andy_role():
    return os.environ['ANDY_ROLE']


def get_Austin_role():
    return os.environ['AUSTIN_ROLE']


def get_Ben_role():
    return os.environ['BEN_ROLE']


def get_Brindle_role():
    return os.environ['BRINDLE_ROLE']


def get_Curtbot_role():
    return os.environ['CURTBOT_ROLE']


def get_Curtis_role():
    return os.environ['CURTIS_ROLE']


def get_Ed_role():
    return os.environ['ED_ROLE']


def get_Finn_role():
    return os.environ['FINN_ROLE']


def get_Joey_role():
    return os.environ['JOEY_ROLE']


def get_Kennedy_role():
    return os.environ['KENNEDY_ROLE']


def get_Kevin_role():
    return os.environ['KEVIN_ROLE']


def get_Logan_role():
    return os.environ['LOGAN_ROLE']


def get_Mike_role():
    return os.environ['MIKE_ROLE']


def get_Nick_role():
    return os.environ['NICK_ROLE']


def get_NickG_role():
    return os.environ['NICKG_ROLE']


def get_Payton_role():
    return os.environ['PAYTON_ROLE']


def get_TribeBlend_role():
    return os.environ['TRIBEBLEND_ROLE']


def get_Vineeth_role():
    return os.environ['VINEETH_ROLE']


def get_Will_role():
    return os.environ['WILL_ROLE']
