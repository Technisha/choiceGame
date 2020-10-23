from ext import yaml, Player, SkillSet

try:
    with open("config.yaml") as f: f.close()
except FileNotFoundError:
    with open("config.yaml", "w+") as f:
        f.write("used: false")

with open("config.yaml") as f:
    config = yaml.load(f)
    try:
        config['used']
    except TypeError:
        config = {}
        config['used'] = False
    if not config['used']:
        config = {
            "used":True,
            "name":input("Hello adventurer! Please enter your name for your character: "),
            "health":100,
            "mana":100,
            "level":0,
            "skills":{
                "speed":0,
                "agility":0,
                "endurance":0,
                "intelligence":0,
                "charisma":0
            },
        "current_choice_code":0
        }
        with open("config.yaml", "w+") as f:
            yaml.dump(config, f)
    with open("config.yaml") as f:
        player = yaml.load(f)
        del(player['used'])
        player['skills'] = SkillSet(**player['skills'])
        player = Player()

print("\nAll data loaded successfully! Have fun!\n")

print(player.Skills.get_intelligence())