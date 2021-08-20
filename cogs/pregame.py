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

  @commands.command(aliases=["j"])
  @commands.guild_only()
  async def join(self,ctx):
    '''Use this to join or create a game.'''
    new_player=assets.Player(str(ctx.author.id),str(ctx.guild.id))
    if str(ctx.guild.id) not in self.bot._arenas.keys():
      new_arena=assets.Arena(ctx.guild.id,ctx.channel.id)
      new_arena.add_player(new_player)
      self.bot._arenas[str(ctx.guild.id)]=new_arena
      await ctx.send("New arena created! You have joined the game! \n**This channel will be the announcement channel for ingame events. Kindly leave and rejoin if you want it to be another chat.**")
    else:
      for player in self.bot._arenas[str(ctx.guild.id)].players:
        if str(ctx.author.id)==player.player_id:
          await ctx.send("You have already joined the game! Type !leave to quit or !votestart to start the game.")
          return
      self.bot._arenas[str(ctx.guild.id)].add_player(new_player)
      await ctx.send(f"You have joined the game! {len(self.bot._arenas[str(ctx.guild.id)].players)} players in the lobby now.")

  @commands.command(aliases=["l"])
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

  @commands.command(aliases=["p","all","players"])
  @commands.guild_only()
  async def list(self,ctx):  
    '''Use this to check the people who have signed up.'''
    if str(ctx.guild.id) not in self.bot._arenas:
      await ctx.send("There is currently no arena in this server. Type !join if you want to start one!")
      return

    temp_msg=await ctx.send("Loading.")
    msg=f"The amount of people signed up are- {len(self.bot._arenas[str(ctx.guild.id)].players)} \n"
    for player in self.bot._arenas[str(ctx.guild.id)].players:
      user=self.bot.get_user(int(player.player_id))
      msg+=f"{user.mention} ({user.name}) \n"
    await temp_msg.edit(content=msg)

  @commands.command(aliases=["start","s","vs"])
  @commands.guild_only()
  async def vstart(self,ctx):  
    '''Use this to vote to start the game.'''
    guild_id=str(ctx.guild.id)
    arena=None
    for _arena in self.bot._arenas:
      if _arena==guild_id:
        arena=self.bot._arenas[_arena]
        break
    if arena==None:
      await ctx.send("Currently there's no arena in this server.")
      return
    if arena.gamestate!=0:
      await ctx.send("There's already a game going on in this server.")
      return

    author=str(ctx.author.id)
    player=None
    for _player in arena.players:
      if _player.player_id==author:
        player=_player
    if player==None:
      await ctx.send("You are currently not in game.")
      return
      
    if player.ready==0:
      player.ready=1
      await ctx.send("You have voted to start the game.")
    elif player.ready==1:
      player.ready=0
      await ctx.send("You have voted to **not** start the game.")

    

def setup(bot):
    bot.add_cog(Pregame(bot))