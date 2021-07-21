#code by top


class Player:

  def __init__(self,player_id,server_id):
    self.server_id=server_id
    self.health=100
    self.strength=0
    self.speed=0
    self.inventory=[]
    self.energy=0
    self.player_id=str(player_id)

  def add_to_inventory(self,item):
    item=item.replace(" ","-").lower()
    self.inventory.append(item)

  def remove_from_inventory(self,item):
    item=item.replace(" ","-").lower()
    if item in self.inventory:
      self.inventory.remove(item)
    else:
      raise Exception("Item not in inventory.")

class Arena:

  def __init__(self,server_id,channel_id):
    self.server_id=str(server_id)
    self.channel_id=str(channel_id)
    self.players=[]
    self.areas=[]
    self.rounds=0
    #gamestate 0=signups, 1=chars, 2=events, 3=day, 4=fights,5=end
    self.gamestate=0

  def add_player(self,player:Player):
    self.players.append(player)

  def remove_player(self,player:Player):
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

