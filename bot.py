# bot.py
import os

from datetime import datetime, timedelta
from discord import Client, Intents
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv

from UniteEnum import UniteInformation, UniteItems
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
async def _ping(ctx: SlashContext):
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")


@slash.slash(
    name="resin_timer",
    description="Allows you to check when your Original Resin resource in Genshin Impact would be fully refreshed",
    guild_ids=GUILD,
    options=[
        create_option(
            name="current_resin_value",
            description="This is how much resin you currently have available",
            option_type=4,
            required=True
        )
    ]
)
async def _resin_time(ctx: SlashContext, current_resin_value: int):
    resin_remaining = 160 - current_resin_value
    minutes_remaining = 10 * resin_remaining
    current_time = datetime.now()

    time_with_full_resin = current_time + timedelta(minutes=minutes_remaining)

    formatted_final_time = time_with_full_resin.strftime("%Y-%m-%d %l:%M %p")
    await ctx.send(f"Your Original Resin ({current_resin_value}/160) will be fully refreshed at {formatted_final_time}")

bot.run(TOKEN)
