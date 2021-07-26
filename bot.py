# bot.py
import os
from discord import Client, Intents
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv

from PiotEnum import UniteInformation, UniteItems
from UniteParser import UniteParser
from utility_functions import convert_string_to_codeblock_string, split_string

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = [int(os.getenv('DISCORD_GUILD'))]

bot = Client(intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Ready!")

@slash.slash(
    name="unite_item", 
    description="Allows you to check information about an item from Pokemon Unite", 
    guild_ids=GUILD,
    options=[
        create_option(
            name="item_name",
            description="This is the item that you want to view stats on.",
            option_type=3,
            required=True,
            choices=[create_choice(name=item, value=item) for item in UniteItems.values_list()]
        ),
        # create_option(
        #     name="show_enhancers_and_dollars",
        #     description="Select this if you want to show the Item Enhancers and Money per level of the item",
        #     option_type=5,
        #     required=True
        # )

    ]
)
async def _unite_item(ctx: SlashContext, item_name: str):
    unite_parser = UniteParser(item_name)
    table_string = unite_parser.read_description_from_csv()
    table_string += unite_parser.read_stats_from_csv()

    for section in split_string(table_string):
        await ctx.send(convert_string_to_codeblock_string(section))
    

@slash.slash(name="ping", guild_ids=GUILD)
async def _ping(ctx): 
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")

bot.run(TOKEN)
