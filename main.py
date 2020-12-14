from time import sleep
from dpcontracts import PreconditionError

from ext import yaml, Entity, Player, Enemy, SkillSet, MoveSet, check_entity, battle # Importing the classes that'll be used in this file
from ext.entities import GlitchTrap, unknown
from ext.enemies import BasicAcidSlime

try: # In this try and except block, i'm checking if 'config.yaml' exists, if it doesn't, then it'll be created
    with open("config.yaml") as f: f.close()
except FileNotFoundError:
    with open("config.yaml", "w+") as f: f.write("used: false") # Writing the default value to this file

with open("config.yaml") as f:
    config = yaml.load(f)
    try:
        config['used'] # Checking if the key exists, as the file might be empty if it was manually created
    except TypeError:
        config = {} 
        config['used'] = False # This'll assign the 'used' key to the `False` value
    if not config['used']: # Here we check if `config['used']` has the value `False`, and if it does, then to continue executing the 'if' block
        config = {
            "used":True, # To state that the config has been edited
            "name":input("Hello adventurer! Please enter your name for your character: "), # Here is an `input` statement, which prompts the user to type in a name for their character
            "health":15, # Default health is 15
            "max_health":15, # Max health is 15
            "mana":15, # Default mana is 15
            "max_mana": 15, # Max mana is 15
            "level":1, #  The default player level
            "skills":{ # Here is just the base stats, they are all at 0 by default
                "speed":0,
                "agility":0,
                "endurance":0,
                "intelligence":0,
                "charisma":0
            },
            "moves":{
                "sword_slash":{
                    "target":Enemy,
                    "range":range(1, 3),
                    "mana_required":0,
                    "description":"Slash enemies with your sword!"
                },
                "heal":{
                    "target":Player,
                    "range":range(6, 10),
                    "mana_required":5,
                    "description":"You can use this to heal yourself, but it uses 5 mana in the process."
                },
                "check":{
                    "target":Enemy,
                    "range":range(0, 1),
                    "mana_required":0,
                    "custom_func":check_entity,
                    "description":"Check enemy stats!"
                }
            },
            "current_choice_code":"", # The current choice code they are on (in-game interactions)
            "relations":{
                "glitchtrap":0
            }
        }
        with open("config.yaml", "w+") as f: # Opening 'config.yaml' in write mode to save the data
            yaml.dump(config, f) # Saving all the data to the file
    with open("config.yaml") as f:
        player = yaml.load(f)
        del(player['used'], player['relations']) # Deleting the 'used' and 'relationships' keys from this dictionary as it can not be used in the 'Player' class when initialising it
        try:
            player['skills'] = SkillSet(**player['skills']) # Initialising the 'SkillSet' class
            player['moves'] = MoveSet(Entity(), **player['moves']) # Initialising the 'MoveSet' class
            error = False
        except PreconditionError: # Here the 'PreconditionError' is catched so i can handle it without the program breaking
            raise SystemExit("There seems to be an issue with the config... Please fix it manually by checking the example config, which can be found here: https://lop.si/lebe")
        player = Player(**player) # Initialising the 'Player' class

print()
unknown.say("All data loaded successfully! Have fun!\n") # Nice message i've put here-

if player.get_current_choice() == '': # The first actual in-game interaction
    '''
    BitchTrap = GlitchTrap.override_name("BitchTrap")
    BitchTrap.say("Welcome! I am {}! And i shall be the one narrating your stor-".format(GlitchTrap.get_name()))
    BitchTrap.say(". . .", delay=0.1)
    BitchTrap.say("Why is my name registered as `{}`...?".format(BitchTrap.get_name()))
    del(BitchTrap)
    unknown.say("*A faint clicking noise can be heard behind you*")
    GlitchTrap.say("There we go! That's fixed! (Fuck you Technisha-)")
    GlitchTrap.say("Anyway, welcome {}, I am {}, and i will be narrating your story, but before we start, let's just check if you're actually listening...".format(player.get_name(), GlitchTrap.get_name()))
    res = GlitchTrap.prompt("Are you listening?", {"1":"Yup! Of course I am!", "2":"Nah, i nodded off as soon as you said your name-"})

    if res == "1":
        GlitchTrap.say("Great!")
        GlitchTrap.set_relation_level(GlitchTrap.get_relation_level()+1)
        unknown.say("*Your relationship with {} has improved, great job!*".format(GlitchTrap.get_name()))

    elif res == "2":
        GlitchTrap.say("...", delay=0.1)
        GlitchTrap.set_relation_level(GlitchTrap.get_relation_level()-1)
        unknown.say("*{} does not like you, congrats on pissing him off already! (I'm definitely annoying him with this later-)*".format(GlitchTrap.get_name()))
        GlitchTrap.say("(I didn't sign up for this goddamn it!)")
        GlitchTrap.say(" Anyway...", delay=0.15)
    GlitchTrap.say("Now let's continue, why don't you try fighting that slime infront of you? It seems relatively easy for a new adventurer like yourself.")
'''
    slime = BasicAcidSlime(name="Basic Acid Slime")
    battle(player, slime)