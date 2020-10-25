from sys import stdout
from time import sleep
from copy import copy
from random import randrange

from yaml import dump, load # This imports the 'dump' and 'load' function from the 'yaml' module
from dpcontracts import require

try: # This is a try and except statement, meaning that it'll try a certain piece of code, and if it errors out (in this case, if it can't import what i need), to do something else
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

'''
        for char in list(' '.join(args)):
            stdout.write(char+sep)
            stdout.flush()
            sleep(0.05)
        stdout.write("\n")
        stdout.flush()
'''

class basicYaml(object): # I'm making a custom class using a different module (a different package that i do not own, but i am allowed to use since it's free to use)
    def __init__(self):
        return

    def dump(self, *args, **kwargs):
        return dump(*args, **kwargs, Dumper=Dumper, sort_keys=False)

    def load(self, *args, **kwargs):
        return load(*args, **kwargs, Loader=Loader)

yaml = basicYaml() # Making an instance of my class, with the name 'yaml'


class SkillSet(object): # This is a class that stores all of the main character stats that will be needed at a later point, i've made functions (basically commands) that'll allow me to fetch/retrive/get the values, or set it instead.
    @require("`speed` must be an integer", lambda args: isinstance(args.speed, int)) # 'require' is a decorator from the 'dpcontracts' module, which allows me to enforce a certain type on any parameter on any function i wont, like how i'm doing it here
    @require("`agility` must be an integer", lambda args: isinstance(args.agility, int))
    @require("`endurance` must be an integer", lambda args: isinstance(args.endurance, int))
    @require("`intelligence` must be an integer", lambda args: isinstance(args.intelligence, int))
    @require("`charisma` must be an integer", lambda args: isinstance(args.charisma, int))
    def __init__(self, speed:int=0, agility:int=0, endurance:int=0, intelligence:int=0, charisma:int=0): # This is the initialise function, which is the most important function in nearly ever class, this is the barebones since it allows you to pass parameters to the class, in this case, the parameters being the skill levels
        self.speed = speed # 'self' is the current class object, meaning everything modified in a specific instance of this class, stays in that instance, i've added 'speed' as an attribute to every new instance of this class, and by default, it's value is 0 unless otherwise specified
        self.agility = agility
        self.endurance = endurance
        self.intelligence = intelligence
        self.charisma = charisma

    def get_speed(self):
        return self.speed # Here i'm returning the speed attribute of this class so i can check it in any part of my code (as long as i have made an instance of this class beforehand)

    def get_agility(self):
        return self.agility

    def get_endurance(self):
        return self.endurance

    def get_intelligence(self):
        return self.intelligence

    def get_charisma(self):
        return self.charisma

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_speed(self, val:int):
        self.speed = val # On this line, i edit the current value of 'self.speed' to match the provided value, 'val'
        with open('config.yaml') as f: # This opens the file called 'config.yaml' in read-only mode
            data = yaml.load(f) # This loads the infomation as a python dictionary, which is basically a collection of keys and values, for example `{"key":"value"}`
            data['skills']['speed'] = val # Here, i also reassign/edit the value of `data['skills']['speed']` to the new value, 'val', which is provided from the function parameters
            with open('config.yaml', "w+") as f: # I'm now reopening 'config.yaml' in write mode, so i can edit the data
                yaml.dump(data, f) # This finally saves the data to the file

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_agility(self, val:int):
        self.agility = val
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['skills']['agility'] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_endurance(self, val:int):
        self.endurance = val
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['skills']['endurance'] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_intelligence(self, val:int):
        self.intelligence = val
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['skills']['intelligence'] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_charisma(self, val:int):
        self.charisma = val
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['skills']['charisma'] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)


class Entity(object): # This is a class to store the entity data, for example, a spider could be an enemy i'll implement at a later point, or it could be an NPC, like a trader or a shop owner
    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    @require("`health` must be an int", lambda args: isinstance(args.health, int))
    @require("`mana` must be an int", lambda args: isinstance(args.mana, int))
    @require("`level` must be an int", lambda args: isinstance(args.level, int))
    @require("`skills` must be an instance of the 'SkillSet' class", lambda args: isinstance(args.skills, SkillSet))
    def __init__(self, name:str="Entity", health:int=100, mana:int=100, level:int=0, skills:SkillSet=SkillSet()):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level
        self.Skills = skills

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_health(self, val:int):
        self.health = val
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['health'] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_mana(self, val:int):
        self.mana = val
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['mana'] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)

    @require("`sep` must be a string", lambda args: isinstance(args.sep, str))
    @require("`delay` must be an integer or a float", lambda args: isinstance(args.delay, float) or isinstance(args.delay, int))
    def say(self, *args, sep:str="", delay=0.05):
        for char in list("["+self.name+"] "+' '.join(args)):
            stdout.write(char+sep)
            stdout.flush()
            sleep(delay)
        stdout.write("\n")
        stdout.flush()

    @require("`question` must be a string", lambda args: isinstance(args.question, str))
    @require("`choices` must be a dictionary/table", lambda args: isinstance(args.choices, dict))
    @require("`delay` must be an integer or a float", lambda args: isinstance(args.delay, float) or isinstance(args.delay, int))
    def prompt(self, question:str, choices:dict, delay:int=0.05): # This is a function that allows me to the user's input so i can get a choice they have selected
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
            self.say("That isn't a valid choice, please enter a VALID choice this time.")
            self.say(question, delay=delay)
        return res


class MoveSet(object):
    def __init__(self, entity:Entity=Entity(), **kwargs):
        if kwargs == {}:
            kwargs = {"punch":range(0, 1)}
        self.entity = entity
        self.moves = kwargs
        for move in self.moves:
            setattr(self, move, self.gen_move_func(move))

    def gen_move_func(self, move):
        # self.moves[move]['mana_required']
        def func():
            deal = randrange(self.moves[move]['range'].start, self.moves[move]['range'].stop)
            if isinstance(self.moves[move]['target'], self.entity):
                pass
            pass
        return func


class NPC(Entity):
    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    @require("`health` must be an int", lambda args: isinstance(args.health, int))
    @require("`mana` must be an int", lambda args: isinstance(args.mana, int))
    @require("`level` must be an int", lambda args: isinstance(args.level, int))
    @require("`skills` must be an instance of the 'SkillSet' class", lambda args: isinstance(args.skills, SkillSet))
    def __init__(self, name:str="NPC", health:int=100, mana:int=100, level:int=0, skills:SkillSet=SkillSet()):
        super(NPC, self).__init__(name, health, mana, level, skills)

    def get_relation_level(self):
        with open('config.yaml') as f:
            data = yaml.load(f)
            relation_level = data['relations'].get(self.name.lower(), None)
            if relation_level == None:
                with open("config.yaml", "w+") as f:
                    data['relations'][self.name.lower()] = 0
                    yaml.dump(data, f)
            return data['relations'][self.name.lower()]

    @require("`val` must be an integer", lambda args: isinstance(args.val, int))
    def set_relation_level(self, val:int):
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['relations'][self.name.lower()] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)

    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    def override_name(self, name:str):
        self = copy(self)
        self.name = name
        return self


class Enemy(Entity):
    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    @require("`health` must be an int", lambda args: isinstance(args.health, int))
    @require("`mana` must be an int", lambda args: isinstance(args.mana, int))
    @require("`level` must be an int", lambda args: isinstance(args.level, int))
    @require("`skills` must be an instance of the 'SkillSet' class", lambda args: isinstance(args.skills, SkillSet))
    @require("`moves` must be an instance of the 'MoveSet' class", lambda args: isinstance(args.moves, MoveSet))
    def __init__(self, name:str="Enemy", health:int=100, mana:int=100, level:int=0, skills:SkillSet=SkillSet(), moves:MoveSet=MoveSet(Entity)):
        super(Enemy, self).__init__(name, health, mana, level, skills)
        moves.Entity = self
        self.Moves = moves


class Player(NPC): # For the 'Player' class, i am inheriting all of the previous functions from the 'NPC' class, and carrying them all here too, since the 'Player' is just a special 'NPC'
    @require("`current_choice_code` must be a string", lambda args: isinstance(args.current_choice_code, str))
    @require("`name` must be a string", lambda args: isinstance(args.name, str))
    @require("`health` must be an int", lambda args: isinstance(args.health, int))
    @require("`mana` must be an int", lambda args: isinstance(args.mana, int))
    @require("`level` must be an int", lambda args: isinstance(args.level, int))
    @require("`skills` must be an instance of the 'SkillSet' class", lambda args: isinstance(args.skills, SkillSet))
    @require("`moves` must be an instance of the 'MoveSet' class", lambda args: isinstance(args.moves, MoveSet))
    def __init__(self, current_choice_code:str="", name:str="Player", health:int=100, mana:int=100, level:int=0, skills:SkillSet=SkillSet(), moves:MoveSet=MoveSet(Entity)):
        super(Player, self).__init__(name, health, mana, level, skills) # This allows me to initialise the 'Entity' class i have used as a base for the 'Player' class, to be loaded into this class's `self` value
        self.current_choice_code = current_choice_code
        self.Moves = moves

    def get_current_choice(self):
        return self.current_choice_code

    @require("`val` must be a string", lambda args: isinstance(args.val, str))
    def set_current_choice(self, val:str):
        self.current_choice_code = val
        with open('config.yaml') as f:
            data = yaml.load(f)
            data['current_choice_code'] = val
            with open('config.yaml', "w+") as f:
                yaml.dump(data, f)