#code by top

import assets

class Arena:

  def __init__(self,server_id):
    self.server_id=str(server_id)
    self.players=[]
    self.areas=[]
    self.rounds=0

  def add_player(self,player:assets.player.Player):
    self.players.append(player)

  def remove_player(self,player:assets.player.Player):
    if player in self.players:
      self.players.remove(player)
    else:
      raise Exception("Player not in list.")

  def add_area(self,area):
    self.areas.append(area)

  def remove_area(self,area):
    if area in self.areas:
      self.players.remove(area)
    else:
      raise Exception("Area not in list.")