# bot.py
import os
from parse_wiki_page import parse_anchors

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    text_channels = '\n - '.join([channel.name for channel in guild.text_channels])
    print(f'Guild text_channels:\n - {text_channels}')
    url = "https://leagueoflegends.fandom.com/wiki/Annie/LoL"
    parse_anchors(url)
    
client.run(TOKEN)
