import json
import random
import sys

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
    print("enc")
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
        r = random.randint(1, d)
        print("d"+str(d)+":\t" + str(r))

        result += r
    for b in bonuses:
        result += b
#        print("bonus:\t" + str(b))
    return result

def d20():
    result = random.randint(1, 20)
    print("d20:\t" + str(result))
    return result

def calcBonus(ability, raw):
    result = raw
    if raw in ["con", "str", "dex", "int", "wis", "cha"]:
        result = (ability[raw]-10)//2
    result = int(result)
    return result

def bonusList(ability, blist):
    result = []
    for item in blist:
        result.append(calcBonus(ability, item))

    return result
#####################################################################################################################################################
initiative = (info["level"]//2) + calcBonus(ability, 'dex')

speed = 6

passiveInsight = 10 + skills["ins"][1] + (info["level"]//2) + calcBonus(ability, 'wis') + skills["ins"][0]

passivePerception = 10 + skills["per"][1] + info["level"]//2 + calcBonus(ability, 'wis') + skills["per"][0]

maxHP = 12 + ability["con"] + 5*(info["level"] - 1)
HP = maxHP
bloodied = False
surgeVal = maxHP // 4
surgePerDay = 6

AC = 10 + info["level"]//2 + 2 + calcBonus(ability, 'dex')
FORT = 10 + info["level"]//2 + 1 + calcBonus(ability, 'str')
REF = 10 + info["level"]//2 + 1 + calcBonus(ability, 'dex')
WILL = 10 + info["level"]//2 + calcBonus(ability, 'wis')

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
        return("acr:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'dex') + skills["acr"][0] + skills["acr"][1]) + "\troll:\t" + str(roll))
    elif skill == "arc":
        roll = d20()
        return("arc:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'int') + skills["arc"][0] + skills["arc"][1]) + "\troll:\t" + str(roll))
    elif skill == "ath":
        roll = d20()
        return("ath:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'str') + skills["ath"][0] + skills["ath"][1]) + "\troll:\t" + str(roll))
    elif skill == "blu":
        roll = d20()
        return("blu:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'cha') + skills["blu"][0] + skills["blu"][1]) + "\troll:\t" + str(roll))
    elif skill == "dip":
        roll = d20()
        return("dip:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'cha') + skills["dip"][0] + skills["dip"][1]) + "\troll:\t" + str(roll))
    elif skill == "dun":
        roll = d20()
        return("dun:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'wis') + skills["dun"][0] + skills["dun"][1]) + "\troll:\t" + str(roll))
    elif skill == "end":
        roll = d20()
        return("end:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'con') + skills["end"][0] + skills["end"][1]) + "\troll:\t" + str(roll))
    elif skill == "hea":
        roll = d20()
        return("hea:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'wis') + skills["hea"][0] + skills["hea"][1]) + "\troll:\t" + str(roll))
    elif skill == "his":
        roll = d20()
        return("his:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'int') + skills["his"][0] + skills["his"][1]) + "\troll:\t" + str(roll))
    elif skill == "ins":
        roll = d20()
        return("ins:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'wis') + skills["ins"][0] + skills["ins"][1]) + "\troll:\t" + str(roll))
    elif skill == "int":
        roll = d20()
        return("int:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'cha') + skills["int"][0] + skills["int"][1]) + "\troll:\t" + str(roll))
    elif skill == "nat":
        roll = d20()
        return("nat:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'wis') + skills["nat"][0] + skills["nat"][1]) + "\troll:\t" + str(roll))
    elif skill == "per":
        roll = d20()
        return("per:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'wis') + skills["per"][0] + skills["per"][1]) + "\troll:\t" + str(roll))
    elif skill == "rel":
        roll = d20()
        return("rel:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'int') + skills["rel"][0] + skills["rel"][1]) + "\troll:\t" + str(roll))
    elif skill == "ste":
        roll = d20()
        return("ste:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'dex') + skills["ste"][0] + skills["ste"][1]) + "\troll:\t" + str(roll))
    elif skill == "str":
        roll = d20()
        return("str:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'cha') + skills["str"][0] + skills["str"][1]) + "\troll:\t" + str(roll))
    elif skill == "thi":
        roll = d20()
        return("thi:\t" + str(roll + info["level"]//2 + calcBonus(ability, 'dex') + skills["thi"][0] + skills["thi"][1]) + "\troll:\t" + str(roll))
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
def showFeats():
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
        show_util(utility)

def show_util(utility):
    for item in utility:
        print("#"+item+":\t"+utility[item])

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
        try:
            pwr = powChoice[pwr]
        except KeyError:
            return
    rolz = []
    atype = 'r'
    if len(pwr) == 3:
        for rol in range(pwr["rattack"][3]):
            d = d20()
            rolz.append((d, d + pwr["rattack"][1] + (calcBonus(ability, pwr["rattack"][0]) + info["level"]//2), pwr["rattack"][2]))
    elif len(pwr) == 5:
        rmChoice = input("Is this (r)anged or (m)elee\n")
        atype = rmChoice
        print("\n")
        if rmChoice == 'r':
            for rol in range(pwr["rattack"][3]):
                d = d20()
                rolz.append((d, d + pwr["rattack"][1] + (calcBonus(ability, pwr["rattack"][0]) + info["level"]//2), pwr["rattack"][2]))
        elif rmChoice == 'm':
            for rol in range(pwr["mattack"][3]):
                d = d20()
                rolz.append((d, d + pwr["mattack"][1] + (calcBonus(ability, pwr["mattack"][0]) + info["level"]//2), pwr["mattack"][2]))
    for num in rolz:
        print("base roll:\t" + str(num[0]))
        print("total roll:\t" + str(num[1]) + "\tvs\t" + str(num[2]))
        print("\n")
    hit = input("did you hit?\n (y)es or (n)o\n")
    print("\n")
    dmg = 0
    if hit == 'y':
        if atype == 'r':
            rblist = bonusList(ability, pwr["ranged"][1])
            dmg = roll(pwr["ranged"][0], rblist)
        elif atype == 'm':
            mblist = bonusList(ability, pwr["melee"][1])
            dmg = roll(pwr["melee"][0], mblist)
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
        if deletion != '':
            print("t")
            try:
                del bag[deletion]
            except KeyError:
                return
    return bag

#################################################################################################################################################################################################
def showInfo(info, ability, skills):
    for item in info:
        print(item + ":\t" + str(info[item]))
    print("\n")
    for item in ability:
        print(item + ":\t" + str(ability[item]))
    print("\n")
    for item in skills:
        print(item + ":\t trained: " + str(skills[item][0]) + "\t misc: " + str(skills[item][1]))
#################################################################################################################################################################################################
def edit_stuff(ability, skills, info, feat, atwill, encounter, daily, utility):
    choice = input("What would you like to edit?\n (a)bility, (s)kills, (i)nfo, (f)eats, (at)will, (e)ncounter, (d)aily, (u)tility\n")
    print("\n")
    if choice == 'a':
        edit_ability(ability)
    elif choice == 's':
        edit_skills(skills)
    elif choice == 'i':
        edit_info(info)
    elif choice == 'f':
        edit_feats(feat)
    elif choice == 'at':
        edit_power(atwill, 'a')
    elif choice == 'e':
        edit_power(encounter, 'e')
    elif choice == 'd':
        edit_power(daily, 'd')
    elif choice == 'u':
        edit_utility()

def edit_ability(ability):
    for item in ability:
        print(item + ":\t" + str(ability[item]))
    abilChoice = input("What ability are you changing?\n")
    print("\n")
    nval = input("What is the new desired value?\n")
    print("\n")
    if nval != '':
        try:
            ability[abilChoice] = int(nval)
        except KeyError:
            return
    abiLoad()

def edit_skills(skills):
    for item in skills:
        print(item + ":\t trained: " + str(skills[item][0]) + "\t misc: " + str(skills[item][1]))
    skilChoice = input("What skill would you like to change?\n")
    print("\n")
    nval = input("What is the new desired value?\n")
    print("\n")
    bonus_type = input("Is this a (t)raining or (m)isc bonus?\n")
    print("\n")
    if bonus_type == 't':
        bonus_type = 0
    elif bonus_type == 'm':
        bonus_type = 1
    else:
        bonus_type = 2
    if bonus_type == 0 or bonus_type == 1:
        if nval != '':
            try:
                skills[skilChoice][bonus_type] = int(nval)
            except KeyError:
                return
    skiLoad()

def edit_info(info):
    for item in info:
        print(item + ":\t" + str(info[item]))
    infoChoice = input("What info would you like to change?\n")
    infoChoice = infoChoice.lower()
    print("\n")
    nval = input("what is the new desired value?\n")
    print("\n")
    if nval != '':
        try:
            if infoChoice == 'xp' or infoChoice == 'level':
                info[infoChoice] = int(nval)
            else:
                info[infoChoice] = nval
        except KeyError:
            return
    infoLoad()

def edit_feats(feat):
    for item in feat:
        print("#"+item+":\t"+feat[item])
    print("\n")
    name = input("What is the name of your new feat \n")
    print("\n")
    effect = input("What is the effect of the new feat\n")
    print("\n")
    if name != '':
        feat[name] = effect
    featLoad()

def edit_utility():
    for item in utility:
        print("#"+item+":\t"+utility[item])
    print("\n")
    name = input("What is the name of your new utility \n")
    print("\n")
    effect = input("What is the effect of the new utility\n")
    print("\n")
    if name != '':
        utility[name] = effect
    utilityLoad()

def edit_power(powObj, typ):
    name = input("What is the name of your power?\n")
    print("\n")
    effect = input("What is the effect of your power?\n")
    print("\n")
    rattack = input("What is your ranged attack? ['3-letter abilty', bonus, 'defense', num-of-rolls]\n")
    print("\n")
    ranged = input("What is your ranged damage? [[#, #, #], ['3-letter ability', #, #]]\n")
    print("\n")
    mattack = input("What is your melee attack? ['3-letter abilty', bonus, 'defense', num-of-rolls]\n")
    print("\n")
    melee = input("What is your melee damage? [[#, #, #], ['3-letter abilty', #, #]]\n")
    print("\n")
    if name != '':
        rattack = eval(rattack)
        ranged = eval(ranged)
        if melee != '' and mattack != '':
            mattack = eval(mattack)
            melee = eval(melee)
    temp = {"effect": effect, "rattack": rattack, "ranged": ranged, "mattack": mattack, "melee": melee}
    print(str(temp["rattack"]))
    if name == '':
        return
    for item in temp:
        if temp[item] != '':
            powObj[name][item] = temp[item]
            print(str(powObj[name][item]))

    if typ == 'a':
        atwill = powObj
        atwillLoad()
    elif typ == 'e':
        enconuter = powObj
        encounterLoad()
    elif typ == 'd':
        daily = powObj
        dailyLoad()

#################################################################################################################################################################################################
def croll():
    dlist = input("What dice are you rolling. (Separate by spaces)\n")
    print("\n")
    dlist = dlist.split(" ")
    for i in dlist:
        print("d"+i+":\t" + str(random.randint(1, int(i))) + "\n")

#################################################################################################################################################################################################
#loop that asks what you want to do. (s)tatus, (c)heck, (h)ealth, (f)eats, (p)ower, (b)ag, (d)ice (i)nfo, (e)dit, (q)uit
while(True):
    print("###############################################################################")
    choice = input("What would you like to do?\n (s)tatus, (c)heck, (h)ealth, (f)eats, (p)ower, (b)ag, (i)nfo, (e)dit, (r)oll, (q)uit\n\n")
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
        showFeats()
    elif choice == 'p':
        print("\n")
        powers(atwill, encounter, daily, utility)
    elif choice == 'b':
        print("\n")
        bag = showBag(bag)
        bagLoad()
    elif choice == 'i':
        print("\n")
        showInfo(info, ability, skills)
    elif choice == 'e':
        print("\n")
        edit_stuff(ability, skills, info, feat, atwill, encounter, daily, utility)
    elif choice == 'r':
        print("\n")
        croll()
    elif choice == 'q':
        sys.exit(0)
    else:
        print("Try again...\n")
    print("\n")
