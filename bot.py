# bot.py
import os

from discord import Client, Intents
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv

from genshin_src.get_refresh_datetime_from_resin_value import get_refresh_datetime_from_resin_value
from genshin_src.get_talent_materials_for_ascenscion import get_talent_materials_for_ascenscion

from pokemon_unite_src.UniteEnum import UniteItems
from pokemon_unite_src.unite_item_print import get_unite_item_table_string_list

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
        )
    ]
)
async def _unite_item(ctx: SlashContext, item_name: str):
    for section in get_unite_item_table_string_list(item_name):
        await ctx.send(section)
    

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
async def _resin_timer(ctx: SlashContext, current_resin_value: int):
    await ctx.send(get_refresh_datetime_from_resin_value(current_resin_value))


@slash.slash(
    name="get_ascenscion_talent_materials",
    description="Allows you to check how many materials need to ascend in Genshin Impact",
    guild_ids=GUILD,
    options=[
        create_option(
            name="current_talent_value",
            description="This is what level you currently have for a talent",
            option_type=4,
            choices=[number for number in range(1,11)],
            required=True
        ),
        create_option(
            name="target_talent_value",
            description="This is what level you want to have for a talent",
            option_type=4,
            choices=[number for number in range(1,11)],
            required=True
        )
    ]
)
async def get_ascenscion_talent_materials(ctx: SlashContext, current_talent_value: int, target_talent_value: int):
    await ctx.send(get_talent_materials_for_ascenscion(current_talent_value, target_talent_value))

bot.run(TOKEN)
