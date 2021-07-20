#code by top

import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Bot

class Events(commands.Cog):

  def __init__(self,bot):
    self.bot=bot

  @commands.Cog.listener()
  async def on_command_error(self,ctx,error):
    await ctx.send(f'```py\n{error.__class__.__name__}: {error}\n```')

def setup(bot):
    bot.add_cog(Events(bot))