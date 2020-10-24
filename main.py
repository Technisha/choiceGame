from dpcontracts import PreconditionError

from ext import yaml, Player, SkillSet # Importing the classes that'll be used in this file

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
            "health":100, # Default health is 100
            "mana":100, # Default mana level is 100
            "level":0, #  The default player level
            "skills":{ # Here is just the base stats, they are all at 0 by default
                "speed":0,
                "agility":0,
                "endurance":0,
                "intelligence":0,
                "charisma":0
            },
        "current_choice_code":"" # The current choice code they are on (in-game interactions)
        }
        with open("config.yaml", "w+") as f: # Opening 'config.yaml' in write mode to save the data
            yaml.dump(config, f) # Saving all the data to the file
    with open("config.yaml") as f:
        player = yaml.load(f)
        del(player['used']) # Deleting the 'used' value from this dictionary as it can not be used in the 'Player' class when initialising it
        error = True
        while error: # I create this loop to catch other potential errors that may have a similar issue
            try:
                player['skills'] = SkillSet(**player['skills']) # Initialising the 'SkillSet' class
                error = False
            except PreconditionError: # Here the 'PreconditionError' is catched so i can handle it without the program breaking
                print("There seems to be an issue with the config... Please fix it manually by checking the example config, which can be found here: https://lop.si/lebe")
                raise SystemExit()
        player = Player(**player) # Initialising the 'Player' class

print("\nAll data loaded successfully! Have fun!\n") # Nice message i've put here-

#@require("`val` must be an integer", lambda args: isinstance(args.val, int))