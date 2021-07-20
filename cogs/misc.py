#code by top

import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Bot

class Misc(commands.Cog):

  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def ping(self,ctx):
    '''Use this to check if the bot is online.'''
    await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(Misc(bot))