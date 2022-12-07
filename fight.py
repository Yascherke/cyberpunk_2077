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


def autoshot(uid, msg):
    find = Finder(uid)
    magazine = find.magazine()

    if magazine[0] >= 3:
        players.update_one({"_id": uid}, {
            "$set": {"magazine": magazine[0] - 2}})
        roll = d20.roll(str(msg))
        return roll
    else:
        return False

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
    find = Finder(uid)
    getHp = find.hpInfo()
    equip = find.equipment()
    dmg = int(msg) - equip[2]

    if dmg <= 0:
        return True
    else:
        hp = getHp[1] - dmg

        players.update_one({"_id": uid}, {
                "$set": {"hp": int(hp)}})

def hit(uid, msg):
    find = Finder(uid)
    magazine = find.magazine()

    if magazine[0] != 0:
        players.update_one({"_id": uid}, {
            "$set": {"magazine": magazine[0] - 1}})
        roll = d20.roll(str(msg))

        return roll
    else:
        return False
    

