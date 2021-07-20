#a bot by top

import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Bot
import asyncio
import random
import os
import time
import datetime
from datetime import date,timedelta
import keep_alive
import inspect
#from cogs.assets import assets
#import assets
#from arena import Arena


token = str(os.environ.get("tokeno"))

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix = ";",intents=intents)
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print("Working boi!")
    bot._arenas={}


if __name__=="__main__":
  cogs_list=["misc","admin","events","pregame"]
  for thing in cogs_list:
    bot.load_extension(f'cogs.{thing}')
  keep_alive.keep_alive()
  bot.run(token)
  