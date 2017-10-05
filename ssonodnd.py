import json
import random

"""
#basic character info
info = {
    "name": "Kraven Moarhed",
    "level": 2,
    "class": "ranger",
    "paragon": "none",
    "epic": "none",
    "xp": 1025,
    "race": "halfling",
    "size": "small",
    "age": "24",
    "gender": "male",
    "height": "4'0",
    "weight": "80 lb",
    "alignment": "chaotic neutral",
    "deity": "Loki"
}

#ability scores
ability = {
    "str": 14,
    "con": 10,
    "dex": 22,
    "int": 12,
    "wis": 14,
    "cha": 13
}

#(skill: trained, misc bonus]
skills = {
    "acrobatics": [True, 2],
    "arcana": [False, 0],
    "athletics": [True, 0],
    "bluff": [False, 0],
    "diplomacy": [False, 0],
    "dungeoneering": [True, 0],
    "endurance": [False, 0],
    "heal": [False, 0],
    "history": [False, 0],
    "insight": [False, 0],
    "intimidate": [False, 0],
    "nature": [True, 0],
    "perception": [True, 0],
    "religion": [False, 0],
    "stealth": [True, 0],
    "streetwise": [False, 0],
    "thievery": [True, 2]
}


#name:{ quantity, value, weight, info)
bag = {
    "gold": {
        "quantity": 111,
        "value": 1,
        "weight": 0,
        "info": "small gold pieces used to purchase things"
    },
    "shortbow": {
        "quantity": 1,
        "value": 25,
        "weight": 3,
        "info": "1d8, shoots arrows with range of 15/30"
    },
    "leather armor": {
        "quantity": 1,
        "value": 25,
        "weight": 15,
        "info": "light armor, AC + dex + 2"
    },
    "adventurer's kit": {
        "quantity": 1,
        "value": 15,
        "weight": 33,
        "info": "backpack, bedroll, flint/steel, rations, rope(50ft), sunrods(2), waterskin"
    },
    "arrows": {
        "quantity": 30,
        "value": 0,
        "weight": 0.1,
        "info": "just regular arrows"
    },
    "thieve's tools": {
        "quantity": 1,
        "value": 20,
        "weight": 1,
        "info": "tools used to thieve, +2 bonus when opening a lock or trap"
    },
    "dagger": {
        "quantity": 2,
        "value": 1,
        "weight": 0.5,
        "info": "1d4, regular dagger"
    },
    "jeweled dice": {
        "quantity": 1,
        "value": 0,
        "weight": 0,
        "info": "bone dice set with jewels. probably magic"
    },
    "book of necromancy": {
        "quantity": 1,
        "value": 0,
        "weight": 1,
        "info": "Book of the undead and stuff"
    }
}




abiLoad = 'ability.json'
with open(abiLoad, 'w') as f_obj:
    json.dump(ability, f_obj)

infoLoad = 'info.json'
with open(infoLoad, 'w') as f_obj:
    json.dump(info, f_obj)

skiLoad = 'skills.json'
with open(skiLoad, 'w') as f_obj:
    json.dump(skills, f_obj)

bagLoad = 'bag.json'
with open(bagLoad, 'w') as f_obj:
    json.dump(bag, f_obj)
"""

###############################################################################################################################

abilDump = 'ability.json'
with open(abilDump) as f_obj:
    ability = json.load(f_obj)

infoDump = 'info.json'
with open(infoDump) as f_obj:
    info = json.load(f_obj)

skillDump = 'skills.json'
with open(skillDump) as f_obj:
    skills = json.load(f_obj)

bagDump = 'bag.json'
with open(bagDump) as f_obj:
    bag = json.load(f_obj)

#returns value of a roll. dice = [dice required for roll], bonuses[bonuses for specific roll]

def roll(dice, bonuses):
    result = 0
    for d in dice:
        result += random.randrange(1, d)
    for b in bonuses:
        result += b
    return result

initiative = (info["level"]/2) + (ability["dex"] - 10)/2

speed = 6

passiveInsight = 10 + skills["insight"][1] + (info["level"]/2) + (ability["wis"] - 10)/2
if skills["insight"][0]:
    passiveInsight += 5

passivePerception = 10 + skills["perception"][1] + info["level"]/2 + (ability["wis"] - 10)/2
if skills["perception"][0]:
    passivePerception += 5

maxHP = 12 + ability["con"] + 5*(info["level"] - 1)
HP = maxHP
bloodied = False
surgeVal = maxHP / 4
surgePerDay = 6

AC = 10 + info["level"]/2 + 2 + (ability["dex"] - 10)/2
FORT = 10 + info["level"]/2 + 1 + (ability["str"] - 10)/2
REF = 10 + info["level"]/2 + 1 + (ability["dex"] - 10)/2
WILL = 10 + info["level"]/2 + (ability["wis"] - 10)/2

weight = 0
for item in bag:
    weight += bag[item]["quantity"] * bag[item]["weight"]

def status():
    print(
        "HP:\t" + str(HP) +"\n" +
        "AC:\t" + str(AC) +"\n" +
        "FORT:\t" + str(FORT) +"\n" +
        "REF:\t" + str(REF) +"\n" +
        "WILL:\t" + str(WILL) +"\n" +
        "initiative:\t" + str(initiative) +"\n" +
        "speed:\t" + str(speed) +"\n"
        "weight:\t" + str(weight) +"\n" +
        "passive insight:\t" + str(passiveInsight) +"\n" +
        "passive perception:\t" + str(passivePerception) +"\n"
    )
def check():
    skill = input("""What would you like to check?\n acrobatics, arcana, athletics, bluff, diplomacy, dungeoneering, endurance, heal,
                    history, insight, intimidate, nature, perception, religion, stealth, streetwise, thievery\n\n""")


#loop that asks what you want to do. (s)tatus, (c)heck, (a)ction, (p)ower, (b)ag, (i)nfo, (e)dit
while(True):
    choice = input("What would you like to do?\n (s)tatus, (c)heck, (a)ction, (p)ower, (b)ag, (i)nfo, (e)dit\n\n")
    if choice == 's' or choice == 'S':
        print("\n")
        status()
    elif choice == 'c' or choice == 'C':
        print("\n")
        check()
    print("\n")
