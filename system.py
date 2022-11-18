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
            
