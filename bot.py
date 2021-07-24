# bot.py
import os
from parse_wiki_page import Parser
from UniteParser import UniteParser

from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = [int(os.getenv('DISCORD_GUILD'))]

bot = Client(intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Ready!")

@slash.slash(name="unite_item",  guild_ids=GUILD)
async def _unite_item(ctx: SlashContext):
    # name = ctx.args[0]
    # parsed_string = UniteParser(name).csv_parse()
    # await ctx.send(parsed_string)

    await ctx.send("Test")

@slash.slash(name="ping", guild_ids=GUILD)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")

bot.run(TOKEN)
