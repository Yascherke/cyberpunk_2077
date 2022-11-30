from pymongo import MongoClient
from mongodb import Finder

cluster = MongoClient(
    "mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test"
)
db = cluster["WoE"]
players = db["players"]
roles = db["class"]
wtypes = db["wtypes"]
weapons = db["weapons"]
armor = db["armor"]
skills = db["skills"]
rockerboys = db["rockerboys"]
solos = db["solos"]
netrunners = db["netrunners"]
techs = db["techs"]
reapers = db["reapers"]
medias = db["medias"]
ekzeks = db["ekzeks"]
police = db["police"]
fixer = db["fixer"]
nomads = db["nomads"]



def getRole(getter):
    for role in roles.find({"Name": getter[0]}):
        rid = role['_id']
        return rid


def getSkill(getter):
    for skill in skills.find({"name": getter}):
        print("Done")
    return [skill['name'],  skill['base'], skill['desc']]


def catchSkill(uid):
    skill_base = []
    for player in players.find({"_id": uid}):
        traits = player["traits"]
        for n in traits:
            print(n)
            x = list(n.values())
            skill_base.append(x)
    return skill_base


def send_money(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player2 = find.money()
    player1 = find.moneyByName(getter[1])
    before = int(player1[0])
    before1 = int(player2[0])
    money = int(getter[0])
    players.update_one({"_id": uid}, {"$set": {"money": before1 - money}})
    players.update_one({"name": getter[1]}, {
                       "$set": {"money": before + money}})


def send_exp(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player = find.generalByName(getter[1])
    exp = int(getter[0])
    players.update_one({"name": getter[1]}, {
                       "$set": {"rank_exp": player[3] + exp}})


def bank(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player = find.moneyByName(getter[1])
    money = int(getter[0])
    players.update_one({"name": getter[1]},
                       {"$set": {
                           "money": player[0] + money
                       }})

def send_ammo(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player2 = find.ammo()
    player1 = find.ammoByName(getter[1])
    before = int(player1[0])
    before1 = int(player2[0])
    money = int(getter[0])
    players.update_one({"_id": uid}, {"$set": {"ammo": before1 - money}})
    players.update_one({"name": getter[1]}, {
                       "$set": {"ammo": before + money}})

def buy_ammo(uid, msg):
    find = Finder(uid)
    player = find.ammo()
    money = find.money()
    before = int(player[0])
    before1 = int(money)
    ammo = int(msg)
    price = ammo * 75
    if money - price >= 0:
        players.update_one({"_id": uid}, {"$set": {"ammo": before1 - price}})
        players.update_one({"_id": uid}, {
                        "$set": {"ammo": before + ammo}})
        return True
    else:
        return False

def giveItem(uid, msg):
    find = Finder(uid)
    getter = msg.replace(' для ', ',').split(',')
    slot = int(getter[0])

    player_bp = find.backpackByName(getter[1])
    owner = find.backpack()

    for_key = slot-1
    owner_item = owner[for_key]

    count = 0
    for item in player_bp:
        if item == 0 and owner_item != 0:
            print(owner_item)
            players.update_one({"name": getter[1]}, {
                "$set": {"slot"+str(count+1): owner_item}})
            players.update_one({"_id": uid}, {
                "$set": {"slot"+str(slot): 0}})
            return True
        elif owner_item == 0:
            return False
        else:
            if count < 10:
                count += 1
            else:
                return False


def equip_wp(uid, msg):

    find = Finder(uid)
    slot = int(msg)
    owner = find.backpack()
    for_key = slot-1
    owner_item = owner[for_key]
    player_wp = find.equipment()

    try:
        getWeapon = find.weapon(owner_item)
        wtype = find.wtype(getWeapon[2])
    except:
        return False

    if owner_item != 0 and player_wp[0] == 0:

        players.update_one({"_id": uid}, {
            "$set": {"weapon": getWeapon[1]}})
        players.update_one({"_id": uid}, {
            "$set": {"max_magazine": wtype[4]}})
        players.update_one({"_id": uid}, {
            "$set": {"slot"+str(slot): 0}})
        return True
    else:
        return False


def equip_armor(uid, msg):

    find = Finder(uid)
    slot = int(msg)
    owner = find.backpack()
    for_key = slot-1
    owner_item = owner[for_key]
    player_armor = find.equipment()
    try:
        getArmor = find.armor(owner_item)
    except:
        return False

    if owner_item != 0 and player_armor[1] == 0:
        if player_armor[1] != 0:
            return 1
        else:
            players.update_one({"_id": uid}, {
                "$set": {"armor": getArmor[1]}})
            players.update_one({"_id": uid}, {
                "$set": {"sp": getArmor[2]}})
            players.update_one({"_id": uid}, {
                "$set": {"slot"+str(slot): 0}})
            return True
    else:
        return False


def output(uid, msg):

    find = Finder(uid)
    player_armor = find.equipment()
    player_wp = find.equipment()
    msg = msg

    if msg == "Броню" or msg == "броню":
        if player_armor[2] != 0:
            players.update_one({"_id": uid}, {
                "$set": {"armor": 0}})
            players.update_one({"_id": uid}, {
                "$set": {"sp": 0}})
        else:
            return False

    if msg == "Оружие" or msg == "оружие":
        if player_wp[0] != 0:
            players.update_one({"_id": uid}, {
                "$set": {"weapon": 0}})
            players.update_one({"_id": uid}, {
                "$set": {"max_magazine": 0}})
            players.update_one({"_id": uid}, {
                "$set": {"magazine": 0}})
            return True
        else:
            return False


def buyWp(uid, msg):
    find = Finder(uid)
    money = find.money()
    player_bp = find.backpack()
    try:
        getWeapon = find.weapon(msg)
        wtype = find.wtype(getWeapon[2])
    except:
        return False

    count = 0
    for item in player_bp:
        if item == 0 and money >= int(wtype[9]):
            players.update_one({"_id": uid}, {
                "$set": {"slot"+str(count+1): getWeapon[1]}})
            players.update_one({"_id": uid}, {
                "$set": {"money": int(money) - int(wtype[9])}})
            return True
        else:
            if count < 10:
                count += 1
            else:
                return False
                
def buyArmor(uid, msg):
    find = Finder(uid)
    money = find.money()
    player_bp = find.backpack()
    try:
        getArmor= find.armor(msg)
    except:
        return False

    count = 0
    for item in player_bp:
        if item == 0 and money >= getArmor[3]:
            players.update_one({"_id": uid}, {
                "$set": {"slot"+str(count+1): getArmor[1]}})
            players.update_one({"_id": uid}, {
                "$set": {"money": int(money) - int(getArmor[3])}})
            return True
        else:
            if count < 10:
                count += 1
            else:
                return False