import d20
from pymongo import MongoClient
from mongodb import Finder

cluster = MongoClient(
    "mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test"
)
db = cluster["WoE"]
players = db["players"]
roles = db["class"]
ranks = db["rank"]
weapons = db["weapons"]
armor = db["armor"]
wtypes = db["wtypes"]


def reloading(uid):
    find = Finder(uid)

    magazine = find.magazine()
    ammo = find.ammo()

    if magazine[0] < magazine[1]:
        players.update_one({"_id": uid}, {
            "$set": {"ammo": ammo[0] - 1}})
        players.update_one({"_id": uid}, {
            "$set": {"magazine": magazine[1]}})
        return True
    else:
        return False

def getDamage(uid, msg):
    getter = msg.replace(' - ', ',').split(',')
    find = Finder(uid)
    getHp = find.hpInfo()
    dmg = int(getter[0]) - int(getter[1])

    if dmg <= 0:
        return True
    else:
        hp = getHp[1] - dmg

        players.update_one({"_id": uid}, {
                "$set": {"hp": int(hp)}})
        return False

def getHealth(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    getHp = find.hpInfo()
    dmg = int(getter[0]) + int(getHp[1])
    if dmg <= getHp[0]:
        players.update_one({"name": getter[1]}, {
                "$set": {"hp": int(dmg)}})
    else:
        players.update_one({"name": getter[1]}, {
                "$set": {"hp": int(getHp[0])}})
        

def hit(uid, msg):
    find = Finder(uid)
    magazine = find.magazine()

    if magazine[0] != 0:
        players.update_one({"_id": uid}, {
            "$set": {"magazine": magazine[0] - int(msg)}})

        return True
    else:
        return False
    

