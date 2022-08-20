# bot.py
import os

from dotenv import load_dotenv
import interactions
from interactions.ext.tasks import create_task, IntervalTrigger

from genshin_src.get_refresh_datetime_from_resin_value import get_refresh_datetime_from_resin_value
from genshin_src.get_talent_materials_for_ascension import get_talent_materials_for_ascension

from pokemon_unite_src.UniteEnum import UniteItems
from pokemon_unite_src.unite_item_print import get_unite_item_table_string_list
from random_src.PlayerNames import PlayerNames
from random_src.generate_roles_for_player_dictionary import generate_roles_for_player_dictionary
from utils.get_list_of_options import get_list_of_options
from utils.check_minecraft_server_status import check_minecraft_server_status, SERVER_OFFLINE_MESSAGE

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = [int(os.getenv('DISCORD_GUILD'))]

bot = interactions.Client(token=TOKEN, default_scope=GUILD)
bot.last_server_status = SERVER_OFFLINE_MESSAGE


@bot.event
async def on_ready():
    _ping_minecraft_server_loop.start()
    print("Ready!")


@bot.command(
    name="check_minecraft_server",
    description="Ping if server is online",
    scope=GUILD,
)
async def _check_minecraft_server(ctx: interactions.CommandContext):
    result_message = check_minecraft_server_status()
    bot.last_server_status = result_message
    await ctx.send(result_message)


@create_task(IntervalTrigger(30))
async def _ping_minecraft_server_loop():
    channel_id_for_status = os.getenv("SERVER_STATUS_CHANNEL_ID")
    bot_author_id = os.getenv("BOT_AUTHOR_ID")
    message = check_minecraft_server_status()

    if message != bot.last_server_status:
        bot.last_server_status = message
        channel = interactions.Channel(**await bot._http.get_channel(channel_id_for_status), _client=bot._http)
        messages = (await channel.get_history())  # ID of bot

        for msg in messages:
            if msg.author.id == bot_author_id:
                await msg.delete()
                break
        await channel.send(message)


@bot.command(
    name="smite_night_roles",
    description="Randomly assigns rolls to each player",
    scope=GUILD,
    options=get_list_of_options(
        number_of_options=5,
        names=[f"player_{num}" for num in range(1, 6)],
        description="Add a player to generate a role for (all options beyond the first are optional",
        types=interactions.OptionType.STRING,
        required=[True] + [False]*5,
        choices=[interactions.Choice(name=name, value=name) for name in PlayerNames.values_list()]
    )
)
async def _smite_night_roles(ctx: interactions.CommandContext, **kwargs):
    result_message = generate_roles_for_player_dictionary(player_dictionary=kwargs)
    await ctx.send(result_message)



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


# @bot.command(
#     name="ascension_talent_materials",
#     description="Allows you to check how many materials need to ascend in Genshin Impact",
#     scope=GUILD,
#     options=[
#         interactions.Option(
#             name="current_talent_value",
#             description="This is what level you currently have for a talent",
#             type=interactions.OptionType.INTEGER,
#             required=True,
#             choices=[number for number in range(1, 11)],
#         ),
#         interactions.Option(
#             name="target_talent_value",
#             description="This is what level you want to have for a talent",
#             type=interactions.OptionType.INTEGER,
#             required=True,
#             choices=[number for number in range(1, 11)]
#         )
#     ]
# )
# async def _ascension_talent_materials(ctx: interactions.CommandContext, current_talent_value: int, target_talent_value: int):
#     await ctx.send(get_talent_materials_for_ascension(current_talent_value, target_talent_value))

bot.start()
