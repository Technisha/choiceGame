from .ext import Entity, NPC, SkillSet, inf

unknown = Entity(name="???")


GlitchTrap = NPC(name="GlitchTrap", health=inf, mana=inf, level=inf, skills=SkillSet(speed=inf, agility=inf, endurance=inf, intelligence=inf, charisma=inf))