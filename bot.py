# bot.py
import os

from discord import Intents
from dotenv import load_dotenv
import interactions

from genshin_src.get_refresh_datetime_from_resin_value import get_refresh_datetime_from_resin_value
from genshin_src.get_talent_materials_for_ascension import get_talent_materials_for_ascension

from pokemon_unite_src.UniteEnum import UniteItems
from pokemon_unite_src.unite_item_print import get_unite_item_table_string_list
from random_src.PlayerNames import PlayerNames
from random_src.generate_role_for_player import generate_role_for_player

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = [int(os.getenv('DISCORD_GUILD'))]

bot = interactions.Client(token=TOKEN, default_scope=GUILD)


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(
    name="smite_night_roles",
    description="Randomly assigns rolls to each player",
    scope=GUILD,
    options=[
            interactions.Option(
                name=f"player_name",
                description="This is the item that you want to view stats on.",
                type=interactions.OptionType.STRING,
                required=True,
                choices=[interactions.Choice(name=item, value=item) for item in PlayerNames.values_list()]
            )
    ]
)
async def _smite_night_roles(ctx: interactions.CommandContext, player_name: str):
    result_message = generate_role_for_player([player_name])
    await ctx.send(result_message)
#

@bot.command(
    name="unite_item",
    description="Allows you to check information about an item from Pokemon Unite",
    scope=GUILD,
    options=[
        interactions.Option(
            name="item_name",
            description="This is the item that you want to view stats on.",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[interactions.Choice(name=item, value=item) for item in UniteItems.values_list()]
        )
    ]
)
async def _unite_item(ctx: interactions.CommandContext, item_name: str):
    for section in get_unite_item_table_string_list(item_name):
        await ctx.send(section)


@bot.command(
    name="resin_timer",
    description="Allows you to check when your Original Resin resource in Genshin Impact would be fully refreshed",
    scope=GUILD,
    options=[
        interactions.Option(
            name="current_resin_value",
            description="This is how much resin you currently have available",
            type=interactions.OptionType.INTEGER,
            required=True
        )
    ]
)
async def _resin_timer(ctx: interactions.CommandContext, current_resin_value: int):
    await ctx.send(get_refresh_datetime_from_resin_value(current_resin_value))


@bot.command(
    name="ascension_talent_materials",
    description="Allows you to check how many materials need to ascend in Genshin Impact",
    scope=GUILD,
    options=[
        interactions.Option(
            name="current_talent_value",
            description="This is what level you currently have for a talent",
            type=interactions.OptionType.INTEGER,
            choices=[number for number in range(1, 11)],
            required=True
        ),
        interactions.Option(
            name="target_talent_value",
            description="This is what level you want to have for a talent",
            type=interactions.OptionType.INTEGER,
            choices=[number for number in range(1, 11)],
            required=True
        )
    ]
)
async def _ascension_talent_materials(ctx: interactions.CommandContext, current_talent_value: int, target_talent_value: int):
    await ctx.send(get_talent_materials_for_ascension(current_talent_value, target_talent_value))

bot.start()
