#code by top
import assets

class Player:

  def __init__(self,player_id,arena:assets.arena.Arena):
    self.arena=arena
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
