import json
import random
import sys


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
    "acr": [5, 2],
    "arc": [0, 0],
    "ath": [5, 0],
    "blu": [0, 0],
    "dip": [0, 0],
    "dun": [5, 0],
    "end": [0, 0],
    "hea": [0, 0],
    "his": [0, 0],
    "ins": [0, 0],
    "int": [0, 0],
    "nat": [5, 0],
    "per": [5, 0],
    "rel": [0, 0],
    "ste": [5, 0],
    "str": [0, 0],
    "thi": [5, 2]
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

##############################################################################################################################################
#returns value of a roll. dice = [dice required for roll], bonuses[bonuses for specific roll]

def roll(dice, bonuses):
    result = 0
    for d in dice:
        result += random.randrange(1, d)
    for b in bonuses:
        result += b
    return result

def d20():
    return random.randrange(1, 20)
#####################################################################################################################################################
initiative = (info["level"]/2) + (ability["dex"] - 10)/2

speed = 6

passiveInsight = 10 + skills["ins"][1] + (info["level"]/2) + (ability["wis"] - 10)/2 + skills["ins"][0]

passivePerception = 10 + skills["per"][1] + info["level"]/2 + (ability["wis"] - 10)/2 + skills["per"][0]

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
#################################################################################################################################################
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
#########################################################################################################################################################################
def check():
    skill = input("""What would you like to check?\n (acr)obatics, (arc)ana, (ath)letics, (blu)ff, (dip)lomacy, (dun)geoneering,\n (end)urance, (hea)l, (his)tory, (ins)ight, (int)imidate, (nat)ure, (per)ception (rel)igion, (ste)alth, (str)eetwise, (thi)every\n\n""")
    print("\n")
    skill = skill.lower()
    result = "That is not a skill you possess..."
    if skill == "acr":
        roll = d20()
        return("acr:\t" + str(roll + info["level"]/2 + (ability["dex"]-10)/2 + skills["acr"][0] + skills["acr"][1]) + "\troll:\t" + str(roll))
    elif skill == "arc":
        roll = d20()
        return("arc:\t" + str(roll + info["level"]/2 + (ability["int"]-10)/2 + skills["arc"][0] + skills["arc"][1]) + "\troll:\t" + str(roll))
    elif skill == "ath":
        roll = d20()
        return("ath:\t" + str(roll + info["level"]/2 + (ability["str"]-10)/2 + skills["ath"][0] + skills["ath"][1]) + "\troll:\t" + str(roll))
    elif skill == "blu":
        roll = d20()
        return("blu:\t" + str(roll + info["level"]/2 + (ability["cha"]-10)/2 + skills["blu"][0] + skills["blu"][1]) + "\troll:\t" + str(roll))
    elif skill == "dip":
        roll = d20()
        return("dip:\t" + str(roll + info["level"]/2 + (ability["cha"]-10)/2 + skills["dip"][0] + skills["dip"][1]) + "\troll:\t" + str(roll))
    elif skill == "dun":
        roll = d20()
        return("dun:\t" + str(roll + info["level"]/2 + (ability["wis"]-10)/2 + skills["dun"][0] + skills["dun"][1]) + "\troll:\t" + str(roll))
    elif skill == "end":
        roll = d20()
        return("end:\t" + str(roll + info["level"]/2 + (ability["con"]-10)/2 + skills["end"][0] + skills["end"][1]) + "\troll:\t" + str(roll))
    elif skill == "hea":
        roll = d20()
        return("hea:\t" + str(roll + info["level"]/2 + (ability["wis"]-10)/2 + skills["hea"][0] + skills["hea"][1]) + "\troll:\t" + str(roll))
    elif skill == "his":
        roll = d20()
        return("his:\t" + str(roll + info["level"]/2 + (ability["int"]-10)/2 + skills["his"][0] + skills["his"][1]) + "\troll:\t" + str(roll))
    elif skill == "ins":
        roll = d20()
        return("ins:\t" + str(roll + info["level"]/2 + (ability["wis"]-10)/2 + skills["ins"][0] + skills["ins"][1]) + "\troll:\t" + str(roll))
    elif skill == "int":
        roll = d20()
        return("int:\t" + str(roll + info["level"]/2 + (ability["cha"]-10)/2 + skills["int"][0] + skills["int"][1]) + "\troll:\t" + str(roll))
    elif skill == "nat":
        roll = d20()
        return("nat:\t" + str(roll + info["level"]/2 + (ability["wis"]-10)/2 + skills["nat"][0] + skills["nat"][1]) + "\troll:\t" + str(roll))
    elif skill == "per":
        roll = d20()
        return("per:\t" + str(roll + info["level"]/2 + (ability["wis"]-10)/2 + skills["per"][0] + skills["per"][1]) + "\troll:\t" + str(roll))
    elif skill == "rel":
        roll = d20()
        return("rel:\t" + str(roll + info["level"]/2 + (ability["int"]-10)/2 + skills["rel"][0] + skills["rel"][1]) + "\troll:\t" + str(roll))
    elif skill == "ste":
        roll = d20()
        return("ste:\t" + str(roll + info["level"]/2 + (ability["dex"]-10)/2 + skills["ste"][0] + skills["ste"][1]) + "\troll:\t" + str(roll))
    elif skill == "str":
        roll = d20()
        return("str:\t" + str(roll + info["level"]/2 + (ability["cha"]-10)/2 + skills["str"][0] + skills["str"][1]) + "\troll:\t" + str(roll))
    elif skill == "thi":
        roll = d20()
        return("thi:\t" + str(roll + info["level"]/2 + (ability["dex"]-10)/2 + skills["thi"][0] + skills["thi"][1]) + "\troll:\t" + str(roll))
    return result
#################################################################################################################################################################################################3
#loop that asks what you want to do. (s)tatus, (c)heck, (a)ction, (p)ower, (b)ag, (i)nfo, (e)dit, (q)uit
while(True):
    choice = input("What would you like to do?\n (s)tatus, (c)heck, (a)ction, (p)ower, (b)ag, (i)nfo, (e)dit, (q)uit\n\n")
    choice = choice.lower()
    if choice == 's':
        print("\n")
        status()
    elif choice == 'c':
        print("\n")
        print(check())
    elif choice == 'q':
        sys.exit(0)
    print("\n")
