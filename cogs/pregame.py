#code by top

import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Bot
from .assets import assets

class Pregame(commands.Cog):

  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def join(self,ctx):
    '''Use this to join or create a game.'''
    new_player=assets.Player(str(ctx.author.id),str(ctx.guild.id))
    if str(ctx.guild.id) not in self.bot._arenas.keys():
      new_arena=assets.Arena(ctx.guild.id)
      new_arena.add_player(new_player)
      self.bot._arenas[str(ctx.guild.id)]=new_arena
      await ctx.send("New arena created! You have joined the game!")
    else:
      for player in self.bot._arenas[str(ctx.guild.id)].players:
        if str(ctx.author.id)==player.player_id:
          await ctx.send("You have already joined the game! Type !leave to quit or !votestart to start the game!")
          return
      self.bot._arenas[str(ctx.guild.id)].add_player(new_player)
      await ctx.send(f"You have joined the game! {len(self.bot._arenas[str(ctx.guild.id)].players)} players in the lobby now.")
      




def setup(bot):
    bot.add_cog(Pregame(bot))