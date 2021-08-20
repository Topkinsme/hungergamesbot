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
  async def on_ready(self):
    print("Working boi!")
    self.bot._arenas={}
    self.game_loop.start()
    
  @commands.Cog.listener()
  async def on_command_error(self,ctx,error):
    await ctx.send(f'```py\n{error.__class__.__name__}: {error}\n```')

  @tasks.loop(minutes=1)
  async def game_loop(self):
    if len(self.bot._arenas)<1:
      return
    arenalist=dict(self.bot._arenas).values()
    for arena in arenalist:
      ready_count=0
      for player in arena.players:
        if player.ready==1:
          ready_count+=1
        if ready_count==len(arena.players):
          arena.phase_done=True
      if arena.gamestate==0:
        #signing up
        if arena.phase_done:
          arena.phase_done=False
          arena.gamestate=1
          arena.timeout_ticks=0
          for player in arena.players:
            player.ready=0
          #more important stuff
          await self.start_game(arena)
        elif arena.timeout_ticks>60:
          channel=self.bot.get_channel(int(arena.channel_id))
          msg=""
          for person in arena.players:
            msg+=f"<@{person.player_id}>"
          self.bot._arenas.pop(str(arena.server_id))
          
          await channel.send(f"This arena has been timed out! It has been deleted.\n{msg}")
        else:
          arena.timeout_ticks+=1
      elif arena.gamestate==1:
        pass

  async def start_game(self,arena):
    channel=self.bot.get_channel(int(arena.channel_id))
    await channel.send("The game has begun!")

def setup(bot):
    bot.add_cog(Events(bot))