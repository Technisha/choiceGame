from random import choices

from dpcontracts import require

from .ext import Entity, Player, Enemy, SkillSet, MoveSet

class BasicAcidSlime(Enemy):
    def __init__(self, name:str="Slime", health:int=10, max_health:int=10, mana:int=12, max_mana:int=12, level:int=1, skills:SkillSet=SkillSet(), moves=None):
        if moves == None:
            moves = MoveSet(self, **{"acid_spit":{"target":Player, "range":{"val":range(1, 4), "weights":[10, 6, 2]}, "mana_required":0, "chance":10}})
        super(BasicAcidSlime, self).__init__(name=name, health=health, max_health=max_health, mana=mana, max_mana=max_mana, level=level, skills=skills, moves=moves)