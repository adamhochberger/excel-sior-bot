# bot.py
import os
# from parse_wiki_page import Parser
from UniteParser import UniteParser, INFO_LIST, ITEMS_LIST

from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv

def split_string(table_string):
    n = 1994
    if len(table_string) > n:
        chunks = []
        i = 0
        while True:
            if len(table_string) - i < n:
                chunk = table_string[i:len(table_string)]
                chunks.append(chunk)
                break
            else:
                newline_position = table_string.rfind("\n", i, i+n)            
                newline_position = newline_position+1
                chunk = table_string[i:newline_position]
                i = newline_position
                chunks.append(chunk)
        
        return chunks
    else:
        return [table_string]    

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = [int(os.getenv('DISCORD_GUILD'))]

bot = Client(intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Ready!")

@slash.slash(name="unite_item", 
    description="Allows you to check information about an item from Pokemon Unite", 
    guild_ids=GUILD,
    options=[
        create_option(
            name="item_name",
            description="This is the item that you want to view stats on.",
            option_type=3,
            required=True,
            choices=[create_choice(name=item, value=item) for item in ITEMS_LIST]
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
    parsed_string = unite_parser.read_description_from_csv()
    parsed_string += unite_parser.read_stats_from_csv()

    for chunk in split_string(parsed_string):
        await ctx.send("```" + chunk + "```")
    

@slash.slash(name="ping", guild_ids=GUILD)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")

bot.run(TOKEN)
