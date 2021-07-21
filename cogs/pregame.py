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
  @commands.guild_only()
  async def join(self,ctx):
    '''Use this to join or create a game.'''
    new_player=assets.Player(str(ctx.author.id),str(ctx.guild.id))
    if str(ctx.guild.id) not in self.bot._arenas.keys():
      new_arena=assets.Arena(ctx.guild.id,ctx.channel.id)
      new_arena.add_player(new_player)
      self.bot._arenas[str(ctx.guild.id)]=new_arena
      await ctx.send("New arena created! You have joined the game! \n**This channel will be the announcement channel for ingame events. Kindly leave and rejoin if u want it to be another chat.**")
    else:
      for player in self.bot._arenas[str(ctx.guild.id)].players:
        if str(ctx.author.id)==player.player_id:
          await ctx.send("You have already joined the game! Type !leave to quit or !votestart to start the game.")
          return
      self.bot._arenas[str(ctx.guild.id)].add_player(new_player)
      await ctx.send(f"You have joined the game! {len(self.bot._arenas[str(ctx.guild.id)].players)} players in the lobby now.")

  @commands.command()
  @commands.guild_only()
  async def leave(self,ctx):   
    '''Use this to leave the game.'''
    for player in self.bot._arenas[str(ctx.guild.id)].players:
        if str(ctx.author.id)==player.player_id:
          self.bot._arenas[str(ctx.guild.id)].remove_player(player)
          if len(self.bot._arenas[str(ctx.guild.id)].players)<1:
            self.bot._arenas.pop(str(ctx.guild.id))
            await ctx.send("You have left the game! Since the arena was empty, it has been deleted.")
          else:
            await ctx.send(f"You have **left** the game! {len(self.bot._arenas[str(ctx.guild.id)].players)} players in the lobby now.")
          return
    else:
      await ctx.send("You were not in the game.")

  @commands.command()
  @commands.guild_only()
  async def list(self,ctx):  
    '''Use this to check the people who have signed up.'''
    temp_msg=await ctx.send("Loading.")
    msg=f"The amount of people signed up are- {len(self.bot._arenas[str(ctx.guild.id)].players)} \n"
    for player in self.bot._arenas[str(ctx.guild.id)].players:
      user=self.bot.get_user(int(player.player_id))
      msg+=f"{user.mention} ({user.name}) \n"
    await temp_msg.edit(content=msg)





def setup(bot):
    bot.add_cog(Pregame(bot))