from pymongo import MongoClient
from mongodb import Finder

cluster = MongoClient(
    "mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test"
)
db = cluster["WoE"]
players = db["players"]
roles = db["class"]
ranks = db["rank"]
cars = db["cars"]
houses = db["house"]
corps = db["corps"]
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
programs = db["programs"]
inventory = db["inventory"]


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
    before = int(player1)
    before1 = int(player2)
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


def bank_gm(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player = find.moneyByName(getter[1])
    money = int(getter[0])
    players.update_one({"name": getter[1]},
                       {"$set": {
                           "money": player + money
                       }})

def bank_pl(uid, msg):
    find = Finder(uid)
    player = find.money()
    money = int(msg)
    players.update_one({"_id": uid},
                       {"$set": {
                           "money": player - money
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
    getter = msg.replace(' тип ', ',').split(',')
    find = Finder(uid)
    player = find.ammo()
    money = find.money()
    before = int(money)
    ammo = int(getter[0])

    if getter[1] == 'Стандартные' and getter[1] == 'Резиновые':
        cost = 10

    if getter[1] == 'Бронебойные' and getter[1] == 'Экспансивные' and getter[1] == 'Светошумовые' and getter[1] == 'Зажигательные' and getter[1] == 'Ядовитые':
        cost = 100

    if getter[1] == 'Биотоксин' and getter[1] == 'ЭМИ' and getter[1] == 'Усыпляющие' and getter[1] == 'Умные':
        cost = 500

    if getter[1] == 'Дымовые' and getter[1] == 'Слезоточивые':
        cost = 50

    price = ammo * cost

    if getter[1] == 'Стандартные' and money - price >= 0:
        players.update_one({"_id": uid}, {"$set": {"ammo": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Бронебойные' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_bb": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Биотоксин' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_toxin": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'ЭМИ' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_emp": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Экспансивные' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_expansive": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Светошумовые' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_stun": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Зажигательные' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_fire": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Ядовитые' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_poison": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Резиновые' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_rubber": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Усыпляющие' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_sleep": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Умные' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_smart": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Дымовые' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_smoke": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
        return True

    elif getter[1] == 'Слезоточивые' and money - price >= 0:
        players.update_one(
            {"_id": uid}, {"$set": {"ammo_eye": player[0] - money}})
        players.update_one({"_id": uid}, {"$set": {"money": before - price}})
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
            players.update_one({"_id": uid}, {
                "$set": {"main_sp": 0}})
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
            if count < 15:
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
    except:
        return False

    if owner_item != 0 and player_wp[0] == 0:

        players.update_one({"_id": uid}, {
            "$set": {"weapon": getWeapon[1]}})
        players.update_one({"_id": uid}, {
            "$set": {"max_magazine": 30}})
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
                "$set": {"main_sp": getArmor[2]}})
            players.update_one({"_id": uid}, {
                "$set": {"slot"+str(slot): 0}})
            return True
    else:
        return False


def buyWp(uid, msg):
    find = Finder(uid)
    money = find.money()
    player_bp = find.backpack()
    getter = msg.replace(' для ', ',').split(',')

    try:
        getWeapon = find.weapon(getter[0])
    except:
        return False

    count = 0
    for item in player_bp:
        if item == 0 and money >= int(getWeapon[3]):
            players.update_one({"name": getter[1]}, {
                "$set": {"slot"+str(count+1): getWeapon[0]}})
            players.update_one({"name": getter[1]}, {
                "$set": {"money": int(money) - int(getWeapon[3])}})
            return True
        else:
            if count < 15:
                count += 1
            else:
                return False


def buyArmor(uid, msg):
    find = Finder(uid)
    money = find.money()
    player_bp = find.backpack()
    getter = msg.replace(' для ', ',').split(',')
    try:
        getArmor = find.armor(getter[0])
    except:
        return False

    count = 0
    for item in player_bp:
        if item == 0 and money >= getArmor[3]:
            players.update_one({"name": getter[1]}, {
                "$set": {"slot"+str(count+1): getArmor[0]}})
            players.update_one({"name": getter[1]}, {
                "$set": {"money": int(money) - int(getArmor[2])}})
            return True
        else:
            if count < 15:
                count += 1
            else:
                return False

