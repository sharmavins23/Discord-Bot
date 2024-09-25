import wordcloud
from discord.ext import commands
import discord
import matplotlib.pyplot as plt
import psycopg2
from .. import tokens as tokens


class Wordcloud(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wordcloud")
    async def wordcloud(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        # Generate then send the matplotlib file
        # https://stackoverflow.com/questions/43145199/create-wordcloud-from-dictionary-values
        db_conn = None
        try:
            db_conn = psycopg2.connect(
                tokens.get_database_url(), sslmode='require'
            )
            cursor = db_conn.cursor()
            cursor.execute("SELECT * FROM wordcloud")
            wordcloud_dict = {}
            for word, count in cursor.fetchall():
                wordcloud_dict[word] = count
            wc = wordcloud.WordCloud(width=800, height=800, max_words=23)
            wc.generate_from_frequencies(wordcloud_dict)
            # https://stackoverflow.com/questions/67010699/unable-to-send-matplotlib-picture-using-discord-py
            filename = "img/wordcloud.png"
            image = discord.File(filename=filename)
            plt.savefig(filename)
            await ctx.send(file=image)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db_conn is not None:
                db_conn.close()
            plt.close()


def onMessageSendWordcloudCount(wordString):
    db_conn = None
    try:
        db_conn = psycopg2.connect(
            tokens.get_database_url(), sslmode='require'
        )
        cursor = db_conn.cursor()
        for word in wordString.split(" "):
            cursor.execute(
                "SELECT * FROM wordcloud WHERE word = %s", (word,)
            )
            if cursor.rowcount == 0:
                cursor.execute(
                    "INSERT INTO wordcloud (word, count) VALUES (%s, 1)", (word,)
                )
            else:
                cursor.execute(
                    "UPDATE wordcloud SET count = count + 1 WHERE word = %s", (
                        word,)
                )
        db_conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()
