from dpcontracts import require

from .ext import Entity, Enemy, SkillSet, MoveSet

class Slime(Enemy):
    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    @require("`health` must be an int", lambda args: isinstance(args.health, int))
    @require("`mana` must be an int", lambda args: isinstance(args.mana, int))
    @require("`level` must be an int", lambda args: isinstance(args.level, int))
    @require("`skills` must be an instance of the 'SkillSet' class", lambda args: isinstance(args.skills, SkillSet))
    @require("`moves` must be an instance of the 'MoveSet' class", lambda args: isinstance(args.moves, MoveSet))
    def __init__(self, name:str="Slime", health:int=100, mana:int=100, level:int=0, skills:SkillSet=SkillSet(), moves:MoveSet=MoveSet(Entity())):
        moves.Entity = self
        super(Slime, self).__init__(name, health, mana, level, skills, moves)