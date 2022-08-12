from discord.ext import commands, tasks
from .. import tokens as tokens
import datetime
from .spotifyfunctions import update_TrBl2
import psycopg2


class SpotifyPassives(commands.Cog):
    # Initialization
    def __init__(self, bot):
        # Initialize bot as self from Cog
        self.bot = bot

        # start up background tasks
        self.tribe_blend_checkup.start()

    # Convert spotify IDs to Discord role IDs
    def spotifyid_to_discordid(self, spot_id):
        # Allows us to use this dictionary as a switch-case of sorts
        return tokens.get_discordid_from_spotifyid(spot_id)

    # Pragosh's background behavior
    @tasks.loop(hours=5)  # running loop every 5 hours
    async def tribe_blend_checkup(self):
        # Grab relevant server channels used to send messages
        bot_chat = self.bot.get_channel(tokens.get_bot_tchat())
        trbl_update_string = "Tribe Blend 2.0 has been updated!"

        try:
            # Connect to the DB
            db_conn = psycopg2.connect(
                tokens.get_database_url(), sslmode='require')
            # Set the cursor
            cur = db_conn.cursor()
            # SELECT the values we want
            cur.execute(
                """
                SELECT updated_date
                FROM tribe_blend_update
                ORDER BY updated_date DESC;
                """)
            # Pull the top output row
            row = cur.fetchone()
            if row is None:
                # Update the playlist because there's no record we have
                update_TrBl2()
                # Make a record of this update
                await bot_chat.send(trbl_update_string)
            else:
                # Check if the last time we updated was over a day ago
                if row[0] < (datetime.datetime.now() - datetime.timedelta(hours=24)):
                    # Update the playlist because it's out of date
                    update_TrBl2()
                    # Make a record of this update
                    await bot_chat.send(trbl_update_string)
            # Close the cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db_conn is not None:
                db_conn.close()

    @tribe_blend_checkup.before_loop
    async def before_printer(self):
        # wait for bot to be online and ready before beginning Tribe Blend Task
        await self.bot.wait_until_ready()
