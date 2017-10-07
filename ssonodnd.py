import json
import random
import sys

atwill = {
    "careful attack": {
        "effect": "ranged or meelee attack",
        "rattack": ("dex", "2", "AC", 1),
        "mattack": ("str", "2", "AC", 1),
        "ranged": ([8], "[0]"),
        "melee": ([4], "[0]")
    },
    "nimble strike": {
        "effect": "shift 1 before or after. ranged attack",
        "attack": ("dex", "0", "AC", 1),
        "ranged": ([8], "[(ability['dex'] - 10)//2]")
    }
}

encounter = {
    "evasive strike": {
        "effect": "shift 1 + wis before or after. ranged or melee attack",
        "rattack": ("dex", "0", "AC", 1),
        "mattack": ("str", "0", "AC", 1),
        "ranged": ([8, 8], "[(ability['dex'] - 10)//2]"),
        "melee": ([4, 4], "[(ability['str'] - 10)//2]")
    }
}

daily = {
    "split tree": {
        "effect": "attack 2 character within 3 spaces. Roll attack twice use higher",
        "attack": ("dex", "0", "AC", 2),
        "ranged": ([8, 8], "[(ability['dex'] - 10)//2]")
    }
}

utility = {
    "second chance": {
        "effect": "DAILY-- When you are hit by an enemy, force them to roll again"
    },
    "crucial advice": {
        "effect": "ENCOUNTER-- An ally gets a bonus to a skill check in a skill you are trained in equal to wis"
    }
}

#ability{name: score}
#info{name: val}
#skills{name: [trained bonus, misc bonus]}
#bag{name: {value:, info:, weight, quantity}}
#power{name:{effect: important stuff
#            attack: (ability, bonus, defense, number of rolls)
#            damage: ([dice], bonus as str)}}
#feat{name: description}

def abiLoad():
    filename = 'ability.json'
    with open(filename, 'w') as f_obj:
        json.dump(ability, f_obj)
def infoLoad():
    filename = 'info.json'
    with open(filename, 'w') as f_obj:
        json.dump(info, f_obj)
def skiLoad():
    filename = 'skills.json'
    with open(filename, 'w') as f_obj:
        json.dump(skills, f_obj)
def bagLoad():
    filename = 'bag.json'
    with open(filename, 'w') as f_obj:
        json.dump(bag, f_obj)
def featLoad():
    filename = 'feat.json'
    with open(filename, 'w') as f_obj:
        json.dump(feat, f_obj)
def atwillLoad():
    filename = 'atwill.json'
    with open(filename, 'w') as f_obj:
        json.dump(atwill, f_obj)
def encounterLoad():
    filename = 'encounter.json'
    with open(filename, 'w') as f_obj:
        json.dump(encounter, f_obj)
def dailyLoad():
    filename = 'daily.json'
    with open(filename, 'w') as f_obj:
        json.dump(daily, f_obj)
def utilityLoad():
    filename = 'utility.json'
    with open(filename, 'w') as f_obj:
        json.dump(utility, f_obj)


###############################################################################################################################
def abilDump():
    filename = 'ability.json'
    with open(filename) as f_obj:
        ability = json.load(f_obj)
        return ability
def infoDump():
    filename = 'info.json'
    with open(filename) as f_obj:
        info = json.load(f_obj)
        return info
def skillDump():
    filename = 'skills.json'
    with open(filename) as f_obj:
        skills = json.load(f_obj)
        return skills
def bagDump():
    filename = 'bag.json'
    with open(filename) as f_obj:
        bag = json.load(f_obj)
        return bag
def featDump():
    filename = 'feat.json'
    with open(filename) as f_obj:
        feat = json.load(f_obj)
        return feat
def atwillDump():
    filename = 'atwill.json'
    with open(filename) as f_obj:
        atwill = json.load(f_obj)
        return atwill
def encounterDump():
    filename = 'encounter.json'
    with open(filename) as f_obj:
        encounter = json.load(f_obj)
        return encounter
def dailyDump():
    filename = 'daily.json'
    with open(filename) as f_obj:
        daily = json.load(f_obj)
        return daily
def utilityDump():
    filename = 'utility.json'
    with open(filename) as f_obj:
        utility = json.load(f_obj)
        return utility


ability = abilDump()
info = infoDump()
skills = skillDump()
bag = bagDump()
feat = featDump()
atwill = atwillDump()
encounter = encounterDump()
daily = dailyDump()
utility = utilityDump()

##############################################################################################################################################
#returns value of a roll. dice = [dice required for roll], bonuses[bonuses for specific roll]

def roll(dice, bonuses):
    result = 0
    for d in dice:
        result += random.randint(1, d)
    for b in bonuses:
        result += b
    return result

def d20():
    return random.randint(1, 20)
#####################################################################################################################################################
initiative = (info["level"]//2) + (ability["dex"] - 10)//2

speed = 6

passiveInsight = 10 + skills["ins"][1] + (info["level"]//2) + (ability["wis"] - 10)//2 + skills["ins"][0]

passivePerception = 10 + skills["per"][1] + info["level"]//2 + (ability["wis"] - 10)//2 + skills["per"][0]

maxHP = 12 + ability["con"] + 5*(info["level"] - 1)
HP = maxHP
bloodied = False
surgeVal = maxHP // 4
surgePerDay = 6

AC = 10 + info["level"]//2 + 2 + (ability["dex"] - 10)//2
FORT = 10 + info["level"]//2 + 1 + (ability["str"] - 10)//2
REF = 10 + info["level"]//2 + 1 + (ability["dex"] - 10)//2
WILL = 10 + info["level"]//2 + (ability["wis"] - 10)//2

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
        return("acr:\t" + str(roll + info["level"]//2 + (ability["dex"]-10)//2 + skills["acr"][0] + skills["acr"][1]) + "\troll:\t" + str(roll))
    elif skill == "arc":
        roll = d20()
        return("arc:\t" + str(roll + info["level"]//2 + (ability["int"]-10)//2 + skills["arc"][0] + skills["arc"][1]) + "\troll:\t" + str(roll))
    elif skill == "ath":
        roll = d20()
        return("ath:\t" + str(roll + info["level"]//2 + (ability["str"]-10)//2 + skills["ath"][0] + skills["ath"][1]) + "\troll:\t" + str(roll))
    elif skill == "blu":
        roll = d20()
        return("blu:\t" + str(roll + info["level"]//2 + (ability["cha"]-10)//2 + skills["blu"][0] + skills["blu"][1]) + "\troll:\t" + str(roll))
    elif skill == "dip":
        roll = d20()
        return("dip:\t" + str(roll + info["level"]//2 + (ability["cha"]-10)//2 + skills["dip"][0] + skills["dip"][1]) + "\troll:\t" + str(roll))
    elif skill == "dun":
        roll = d20()
        return("dun:\t" + str(roll + info["level"]//2 + (ability["wis"]-10)//2 + skills["dun"][0] + skills["dun"][1]) + "\troll:\t" + str(roll))
    elif skill == "end":
        roll = d20()
        return("end:\t" + str(roll + info["level"]//2 + (ability["con"]-10)//2 + skills["end"][0] + skills["end"][1]) + "\troll:\t" + str(roll))
    elif skill == "hea":
        roll = d20()
        return("hea:\t" + str(roll + info["level"]//2 + (ability["wis"]-10)//2 + skills["hea"][0] + skills["hea"][1]) + "\troll:\t" + str(roll))
    elif skill == "his":
        roll = d20()
        return("his:\t" + str(roll + info["level"]//2 + (ability["int"]-10)//2 + skills["his"][0] + skills["his"][1]) + "\troll:\t" + str(roll))
    elif skill == "ins":
        roll = d20()
        return("ins:\t" + str(roll + info["level"]//2 + (ability["wis"]-10)//2 + skills["ins"][0] + skills["ins"][1]) + "\troll:\t" + str(roll))
    elif skill == "int":
        roll = d20()
        return("int:\t" + str(roll + info["level"]//2 + (ability["cha"]-10)//2 + skills["int"][0] + skills["int"][1]) + "\troll:\t" + str(roll))
    elif skill == "nat":
        roll = d20()
        return("nat:\t" + str(roll + info["level"]//2 + (ability["wis"]-10)//2 + skills["nat"][0] + skills["nat"][1]) + "\troll:\t" + str(roll))
    elif skill == "per":
        roll = d20()
        return("per:\t" + str(roll + info["level"]//2 + (ability["wis"]-10)//2 + skills["per"][0] + skills["per"][1]) + "\troll:\t" + str(roll))
    elif skill == "rel":
        roll = d20()
        return("rel:\t" + str(roll + info["level"]//2 + (ability["int"]-10)//2 + skills["rel"][0] + skills["rel"][1]) + "\troll:\t" + str(roll))
    elif skill == "ste":
        roll = d20()
        return("ste:\t" + str(roll + info["level"]//2 + (ability["dex"]-10)//2 + skills["ste"][0] + skills["ste"][1]) + "\troll:\t" + str(roll))
    elif skill == "str":
        roll = d20()
        return("str:\t" + str(roll + info["level"]//2 + (ability["cha"]-10)//2 + skills["str"][0] + skills["str"][1]) + "\troll:\t" + str(roll))
    elif skill == "thi":
        roll = d20()
        return("thi:\t" + str(roll + info["level"]//2 + (ability["dex"]-10)//2 + skills["thi"][0] + skills["thi"][1]) + "\troll:\t" + str(roll))
    return result
#####################################################################################################################################################################################################
def health(HP, maxHP):
    healthChoice = input("Would you like to (a)dd or (s)ubtract health?\n")
    print("\n")
    amount = input("How much?\n")
    print("\n")
    if healthChoice == 'a':
        HP += int(amount)
        if HP > maxHP:
            HP = maxHP
    elif healthChoice == 's':
        HP -= int(amount)
    print("You have " + str(HP) + " HP\n")
    return HP
######################################################################################################################################################################################################
def feats():
    for item in feat:
        print("#" + item + ":\t" + feat[item])
################################################################################################################################################################################################
def powers(atwill, encounter, daily, utility):
    powChoice = input("Which powers would you like to see?\n (a)t-will, (e)ncounter, (d)aily, (u)tility\n")
    powChoice = powChoice.lower()
    print("\n")
    if powChoice == 'a':
        print("\n")
        show(atwill)
        usePower(atwill)
    elif powChoice == 'e':
        print("\n")
        show(encounter)
        usePower(encounter)
    elif powChoice == 'd':
        print("\n")
        show(daily)
        usePower(daily)
    elif powChoice == 'u':
        print("\n")
        show(utility)

def show(choice):
        for item in choice:
            print(item + ":\n")
            for att in choice[item]:
                print("\t" + att + ":\t" + str(choice[item][att]))
            print("\n")

def usePower(powChoice):
    print("\n")
    pwr = input("What power would you like to use?\n")
    print("\n")
    if pwr != '':
        pwr = pwr.lower()
        pwr = powChoice[pwr]
    rolz = []
    atype = 'r'
    if len(pwr) == 3:
        for rol in range(pwr["attack"][3]):
            d = d20()
            rolz.append((d, d + int(pwr["attack"][1]) + (ability[pwr["attack"][0]] - 10)//2))
    elif len(pwr) == 5:
        rmChoice = input("Is this (r)anged or (m)elee\n")
        atype = rmChoice
        print("\n")
        if rmChoice == 'r':
            for rol in range(pwr["rattack"][3]):
                d = d20()
                rolz.append((d, d + int(pwr["rattack"][1]) + (ability[pwr["rattack"][0]] - 10)//2))
        elif rmChoice == 'm':
            for rol in range(pwr["mattack"][3]):
                d = d20()
                rolz.append((d, d + int(pwr["mattack"][1]) + (ability[pwr["mattack"][0]] - 10)//2))
    for num in rolz:
        print("base roll:\t" + str(num[0]))
        print("total roll:\t" + str(num[1]))
        print("\n")
    hit = input("did you hit?\n (y)es or (n)o\n")
    print("\n")
    dmg = 0
    if hit == 'y':
        if atype == 'r':
            dmg = roll(pwr["ranged"][0], eval(pwr["ranged"][1]))
        elif atype == 'm':
            dmg = roll(pwr["melee"][0], eval(pwr["melee"][1]))
    print("damage:\t" + str(dmg))
##################################################################################################################################################################################################
def showBag(bag):
    for item in bag:
        print(item + ":\t" + bag[item]["info"])
        print("quantity:\t" + str(bag[item]["quantity"]))
        print("value:\t" + str(bag[item]["value"]))
        print("\n")
    mod = input("would you like to edit an item, delete an item or add a new one?\n (e)dit, (a)dd, (d)elete\n")
    if mod == 'e':
        edition = input("What item are you editing?\n")
        print("\n")
        if edition in bag.keys():
            attToEdit = input("Are you editing (v)alue, (q)uantity, or (i)nfo\n")
            print("\n")
            newVal = input("What is the new value(" + attToEdit +")?\n")
            print("\n")
            if newVal != '':
                if attToEdit == 'v':
                    bag[edition]["value"] = int(newVal)
                elif attToEdit == 'q':
                    bag[edition]["quantity"] = int(newVal)
                elif attToEdit == 'i':
                    bag[edition]["info"] = newVal
    elif mod == 'a':
        name = input("what is the item's name?\n")
        print("\n")
        description = input("what is the item's description?\n")
        print("\n")
        quantity = input("what is the item's quantity?\n")
        print("\n")
        value = input("what is the item's value\n")
        print("\n")
        if(name != '' and description != '' and quantity != '' and value != ''):
            bag[name] = {"value": int(value), "quantity": int(quantity), "info": description}
    elif mod == 'd':
        deletion = input("Which item are you deleting?\n")
        print("\n")
        try:
            del bag[deletion]
        except KeyError:
            pass
    return bag

#################################################################################################################################################################################################
def showInfo(info):
    for item in info:
        print(item + ":\t" + str(info[item]))
#################################################################################################################################################################################################
def edit_stuff(ability):
    print("Your stuff is totes editted")
#################################################################################################################################################################################################
#loop that asks what you want to do. (s)tatus, (c)heck, (h)ealth, (f)eats, (p)ower, (b)ag, (d)ice (i)nfo, (e)dit, (q)uit
while(True):
    print("###############################################################################")
    choice = input("What would you like to do?\n (s)tatus, (c)heck, (h)ealth, (f)eats, (p)ower, (b)ag, (i)nfo, (e)dit, (q)uit\n\n")
    choice = choice.lower()
    if choice == 's':
        print("\n")
        status()
    elif choice == 'c':
        print("\n")
        print(check())
    elif choice == 'h':
        print("\n")
        HP = health(HP, maxHP)
    elif choice == 'f':
        print("\n")
        feats()
    elif choice == 'p':
        print("\n")
        powers(atwill, encounter, daily, utility)
    elif choice == 'b':
        print("\n")
        bag = showBag(bag)
        bagLoad()
    elif choice == 'i':
        print("\n")
        showInfo(info)
    elif choice == 'e':
        print("\n")
        edit_stuff(ability)
    elif choice == 'q':
        sys.exit(0)
    else:
        print("Try again...\n")
    print("\n")
