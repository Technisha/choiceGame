from sys import stdout
from time import sleep
from copy import copy
from random import randrange, choices

from yaml import dump, load # This imports the 'dump' and 'load' function from the 'yaml' module
from dpcontracts import require
try: # This is a try and except statement, meaning that it'll try a certain piece of code, and if it errors out (in this case, if it can't import what i need), to do something else
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from .exceptions import NotEnoughMana

'''
        for char in list(' '.join(args)):
            stdout.write(char+sep)
            stdout.flush()
            sleep(0.05)
        stdout.write("\n")
        stdout.flush()
'''

inf=float("inf")

class basicYaml(object): # I'm making a custom class using a different module (a different package that i do not own, but i am allowed to use since it's free to use)
    def __init__(self):
        return

    def dump(self, *args, **kwargs):
        return dump(*args, **kwargs, Dumper=Dumper, sort_keys=False)

    def load(self, *args, **kwargs):
        return load(*args, **kwargs, Loader=Loader)

yaml = basicYaml() # Making an instance of my class, with the name 'yaml'


class SkillSet(object): # This is a class that stores all of the main character stats that will be needed at a later point, i've made functions (basically commands) that'll allow me to fetch/retrive/get the values, or set it instead.
    @require("`speed` must be an integer", lambda args: isinstance(args.speed, int) or (args.speed, float)) # 'require' is a decorator from the 'dpcontracts' module, which allows me to enforce a certain type on any parameter on any function i wont, like how i'm doing it here
    @require("`agility` must be an integer", lambda args: isinstance(args.agility, int) or (args.agility, int))
    @require("`endurance` must be an integer", lambda args: isinstance(args.endurance, int) or (args.endurance, float))
    @require("`intelligence` must be an integer", lambda args: isinstance(args.intelligence, int) or (args.intelligence, float))
    @require("`charisma` must be an integer", lambda args: isinstance(args.charisma, int) or (args.charisma, float))
    def __init__(self, speed:int=0, agility:int=0, endurance:int=0, intelligence:int=0, charisma:int=0, file:str=''): # This is the initialise function, which is the most important function in nearly ever class, this is the barebones since it allows you to pass parameters to the class, in this case, the parameters being the skill levels
        if file == '':
            self._file = file
        else:
            self._file = file
        self._speed = speed # 'self' is the current class object, meaning everything modified in a specific instance of this class, stays in that instance, i've added 'speed' as an attribute to every new instance of this class, and by default, it's value is 0 unless otherwise specified
        self._agility = agility
        self._endurance = endurance
        self._intelligence = intelligence
        self._charisma = charisma

    def get_speed(self):
        return self._speed # Here i'm returning the speed attribute of this class so i can check it in any part of my code (as long as i have made an instance of this class beforehand)

    def get_agility(self):
        return self._agility

    def get_endurance(self):
        return self._endurance

    def get_intelligence(self):
        return self._intelligence

    def get_charisma(self):
        return self._charisma

    @require("`val` must be an integer", lambda args: isinstance(args.val, int) or (args.val, float))
    def set_speed(self, val:int):
        self._speed = val # On this line, i edit the current value of 'self.speed' to match the provided value, 'val'
        if not self._file: return
        with open(self._file) as f: # This opens the file called 'config.yaml' in read-only mode
            data = yaml.load(f) # This loads the infomation as a python dictionary, which is basically a collection of keys and values, for example `{"key":"value"}`
            data['skills']['speed'] = val # Here, i also reassign/edit the value of `data['skills']['speed']` to the new value, 'val', which is provided from the function parameters
            with open(self._file, "w+") as f: # I'm now reopening 'config.yaml' in write mode, so i can edit the data
                yaml.dump(data, f) # This finally saves the data to the file

    @require("`val` must be an integer", lambda args: isinstance(args.val, int) or (args.val, float))
    def set_agility(self, val:int):
        self._agility = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['skills']['agility'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int) or (args.val, float))
    def set_endurance(self, val:int):
        self._endurance = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['skills']['endurance'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int) or (args.val, float))
    def set_intelligence(self, val:int):
        self._intelligence = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['skills']['intelligence'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int) or (args.val, float))
    def set_charisma(self, val:int):
        self._charisma = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['skills']['charisma'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)


class Entity(object): # This is a class to store the entity data, for example, a spider could be an enemy i'll implement at a later point, or it could be an NPC, like a trader or a shop owner
    @require("`file` must be a string", lambda args: isinstance(args.file, str))
    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    @require("`health` must be an int", lambda args: isinstance(args.health, int) or (args.health, float))
    @require("`max_health` must be an int", lambda args: isinstance(args.max_health, int) or (args.max_health, float))
    @require("`mana` must be an int", lambda args: isinstance(args.mana, int) or (args.mana, float))
    @require("`max_mana` must be an int", lambda args: isinstance(args.max_mana, int) or (args.max_mana, float))
    @require("`level` must be an int", lambda args: isinstance(args.level, int) or (args.level, float))
    @require("`skills` must be an instance of the 'SkillSet' class", lambda args: isinstance(args.skills, SkillSet))
    def __init__(self, file:str='', name:str="Entity", health:int=15, max_health:int=15, max_mana:int=15, mana:int=15, level:int=0, skills:SkillSet=SkillSet()):
        self._file = file
        if file == '': self._file = None
        self._name = name
        self._health = health
        self._max_health = max_health
        self._mana = mana
        self._max_mana = max_mana
        self._level = level
        skills._file = self._file
        self.Skills = skills

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def get_max_health(self):
        return self._max_health

    def get_max_mana(self):
        return self._max_mana

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_health(self, val:int):
        if (val) >= self._max_health:
            val = self._max_health
        elif (val) <= 0:
            val = 0
        self._health = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['health'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_mana(self, val:int):
        if (val) >= self._max_mana:
            val = self._max_mana
        elif (val) <= 0:
            val = 0
        self._mana = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['mana'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_max_health(self, val:int):
        self._max_health = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['max_health'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_max_mana(self, val:int):
        self._max_mana = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['max_mana'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)

    @require("`sep` must be a string", lambda args: isinstance(args.sep, str))
    @require("`delay` must be an integer or a float", lambda args: isinstance(args.delay, float) or isinstance(args.delay, int))
    def say(self, *args, sep:str="", delay=0.05):
        for char in list("["+self.get_name()+"] "+' '.join(args)):
            stdout.write(char+sep)
            stdout.flush()
            sleep(delay)
        stdout.write("\n")
        stdout.flush()

    @require("`question` must be a string", lambda args: isinstance(args.question, str))
    @require("`choices` must be a dictionary/table", lambda args: isinstance(args.choices, dict))
    @require("`delay` must be an integer or a float", lambda args: isinstance(args.delay, float) or isinstance(args.delay, int))
    @require("`invalid_choice` must be a string", lambda args: isinstance(args.invalid_choice, str))
    def prompt(self, question:str, choices:dict, delay:int=0.05, invalid_choice:str="That isn't a valid choice, please enter a VALID choice this time."): # This is a function that allows me to the user's input so i can get a choice they have selected
        self.say(question, delay=delay)
        a = []
        t = choices
        for key in choices:
            a.append(key+": "+choices[key])
        choices = a
        del(a)
        for char in list('\n'.join(choices)):
            stdout.write(char)
            stdout.flush()
            sleep(delay)
        stdout.write("\n")
        stdout.flush()
        while True:
            res = input()
            if res in t:
                del(t)
                break
            self.say(invalid_choice, delay=delay)
            self.say(question, delay=delay)
        return res


class MoveSet(object):
    @require("`entity` must be a subclass of the `Entity` class, examples: `Enemy` or `Player`", lambda args: issubclass(type(args.entity), Entity))
    def __init__(self, entity:Entity, **kwargs):
        self._entity = entity
        self._moves = kwargs # Each move should be in a format like this: `moveName={"target":classThatInheritsFromEntity, "range":range(minDmg, maxDmg), "mana_required":manaRequiredAsInt}` or `**{"moveName":{"target":classThatInheritsFromEntity, "range":range(minDmg, maxDmg), "mana_required":manaRequiredAsInt, "description":DescriptionAsAString}}`
        for move in self._moves:
            setattr(self, move, self.__gen_move_func__(move))

    def __gen_move_func__(self, move):
        def func(target, *args, **kwargs):
            if (self._entity.get_mana()-self._moves[move]['mana_required']) < 0:
                raise NotEnoughMana("The `{}` of type `{}` does not have enough Mana to perform this move!".format(self._entity.get_name(), type(self._entity).__name__))
            self._entity.set_mana(self._entity.get_mana()-self._moves[move]['mana_required'])
            if type(self._moves[move]['range']) == dict:
                deal = choices([*self._moves[move]['range']['val']], weights=self._moves[move]['range']['weights'])[0]
            else:
                deal = randrange(self._moves[move]['range'].start, self._moves[move]['range'].stop, self._moves[move]['range'].step)
            if self._moves[move].get("custom_func", False):
                self._moves[move]["custom_func"](*args, self=self, target=target, **kwargs)
            if issubclass(type(self._entity), self._moves[move]['target']):
                self._entity.set_health(self._entity.get_health()+deal)
                return
            target.set_health(target.get_health()-deal)
            return
        return func

    def __get_all_moves__(self):
        return self._moves.keys()

    def __get_move__(self, move):
        return getattr(self, move)


class NPC(Entity):
    def __init__(self, name:str="NPC", *args, **kwargs):
        super(NPC, self).__init__(file='', name=name, *args, **kwargs)

    def get_relation_level(self):
        with open('config.yaml') as f:
            data = yaml.load(f)
            relation_level = data['relations'].get(self._name.lower(), None)
            if relation_level == None:
                with open("config.yaml", "w+") as f:
                    data['relations'][self._name.lower()] = 0
                    yaml.dump(data, f)
            return data['relations'][self._name.lower()]

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_relation_level(self, val:int):
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['relations'][self._name.lower()] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)

    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    def override_name(self, name:str):
        self = copy(self)
        self._name = name
        return self


class Player(Entity): # For the 'Player' class, i am inheriting all of the previous functions from the 'Entity' class, and carrying them all here too, since the 'Player' is just a special 'Entity'
    @require("`current_choice_code` must be a string", lambda args: isinstance(args.current_choice_code, str))
    def __init__(self, current_choice_code:str="", name:str="Player", moves:MoveSet=None, file:str="config.yaml", *args, **kwargs):
        super(Player, self).__init__(file=file, name=name, *args, **kwargs) # This allows me to initialise the 'Entity' class i have used as a base for the 'Player' class, to be loaded into this class's `self` value
        self._current_choice_code = current_choice_code
        if moves == None:
            moves = MoveSet(self)
        self.Moves = moves

    def get_current_choice(self):
        return self._current_choice_code

    @require("`val` must be a string", lambda args: isinstance(args.val, str))
    def set_current_choice(self, val:str):
        self._current_choice_code = val
        if not self._file: return
        with open(self._file) as f:
            data = yaml.load(f)
            data['current_choice_code'] = val
            with open(self._file, "w+") as f:
                yaml.dump(data, f)


class Enemy(Entity):
    def __init__(self, name:str="Enemy", moves:MoveSet=None, *args, **kwargs):
        super(Enemy, self).__init__(file='', name=name, *args, **kwargs)
        if moves == None:
            moves = MoveSet(self, **{"punch":{"range":range(0, 2), "mana_required":0, "target":Player}})
        self.Moves = moves

    def __rand_move__(self):
        Attacks = []
        Weights = []
        for move in [f for f in dir(self.Moves) if not f.startswith('_')]:
            Weights.append(self.Moves._moves[move].get('chance', 0))
            Attacks.append(move)
        return choices(Attacks, weights=Weights)[0]


def check_entity(self, target, narrator=Entity(name="???")):
    narrator.say("{} has `{}` out of `{}` hp, `{}` out of `{}` mp, and it has the following moves:".format(target.get_name(), target.get_health(), target.get_max_health(), target.get_mana(), target.get_max_mana()), delay=0.025)
    for i in target.Moves.__get_all_moves__():
        narrator.say(i, delay=0.025)
    print()

def list_type_checker(args):
    T = []
    for enemy in args.enemies:
        if issubclass(type(enemy), Enemy):
            T.append(True)
        else:
            T.append(False)
    if False not in T:
        return True
    return False

@require("`player` must be an instance of the `Player` class", lambda args: isinstance(args.player, Player))
@require("`enemies` must be a list of `Enemy` classes", list_type_checker)
def battle(player:Player, *enemies, battleNarrator:Entity=Entity(name="???")):
    enemies = list(enemies)
    battling = True
    if len(enemies) > 1:
        battleNarrator.say("*There are {} enemies, better be careful!*".format(len(enemies)))
    else:
        battleNarrator.say("*There is only 1 enemy, so it should be easy to take down, give it your all!*")
    battleNarrator.say("*First turn is yours!*", delay=0.02)
    while battling:
        moves = {}
        for move in [f for f in dir(player.Moves) if not f.startswith('_')]:
            moves[move] = player.Moves._moves[move].get("description", str(None))
        check = True
        while check:
            T = battleNarrator.prompt(question="Here is your current moveset, to use a move just type it's name and press enter!", choices=moves, delay=0.02, invalid_choice="Sorry, that isn't a valid move, please try again!").lower()
            if T != "check":
                check = False
            move = copy(player.Moves._moves[T])
            move["name"] = T
            del(T)
            if move["target"] == type(player):
                player.Moves.__get_move__(move["name"])(player)
                battleNarrator.say("You used `{}` on yourself, your health is now `{}/{}` and your mana is now at `{}/{}`\n".format(move["name"], player.get_health(), player.get_max_health(), player.get_mana(), player.get_max_mana()))
            else:
                if len(enemies) > 1:
                    T = {}
                    for i in range(0, len(enemies)):
                        T[str(i)] = enemies[i].get_name()
                    enemy = enemies[int(battleNarrator.prompt("Which enemy will you use `{}` on?".format(move["name"]), T, delay=0.02, invalid_choice="That isn't a valid enemy, please choose an enemy from the list"))]
                    if check:
                        player.Moves.__get_move__(move["name"])(enemy)
                    else: 
                        battleNarrator.say("{} currently has {} hp out of {}".format(enemy.get_name(), enemy.get_health(), enemy.get_max_health()), delay=0.02)
                        player.Moves.__get_move__(move["name"])(enemy)
                        battleNarrator.say("{} now has {} hp after being hit by `{}`".format(enemy.get_name(), enemy.get_health(), move["name"]), delay=0.02)
                        for enemy in enemies:
                            if enemy.get_health() == 0:
                                battleNarrator.say("{0} has fainted! {0} is now unable to battle!".format(enemy.get_name()), delay=0.02)
                else:
                    enemy = enemies[0]
                    if check:
                        player.Moves.__get_move__(move["name"])(enemy)
                    else:
                        battleNarrator.say("{} currently has {} hp out of {}".format(enemy.get_name(), enemy.get_health(), enemy.get_max_health()), delay=0.02)
                        player.Moves.__get_move__(move["name"])(enemy)
                        battleNarrator.say("{} now has {} hp after being hit by `{}`".format(enemy.get_name(), enemy.get_health(), move["name"]), delay=0.02)
                        if not bool(enemy.get_health()):
                            battleNarrator.say("{0} has fainted! {0} is now unable to battle!\n".format(enemy.get_name()), delay=0.02)
        for enemy in enemies:
            if not bool(player.get_health()):
                break
            move = enemy.__rand_move__()
            battleNarrator.say("{}'s turn,".format(enemy.get_name()), delay=0.025)
            if issubclass(type(enemy), enemy.Moves._moves[move]["target"]):
                T = enemies[randrange(0, len(enemies))]
                enemy.Moves.__get_move__(move)(T)
                battleNarrator.say("{0} used `{1}` on {2}! {2} now has {3} hp out of {4}!".format(enemy.get_name(), move, T.get_name(), T.get_health(), T.get_max_health()), delay=0.025)
                enemy.__get_move__(move)(T)
            else:
                enemy.Moves.__get_move__(move)(player)
                battleNarrator.say("{} used `{}` on you! You now have {} out of {} hp!\n".format(enemy.get_name(), move, player.get_health(), player.get_max_health()), delay=0.025)
        if not bool(player.get_health()):
            battleNarrator.say("{} has fainted! You'll need to restart the game and try again next time... Good luck!")
            