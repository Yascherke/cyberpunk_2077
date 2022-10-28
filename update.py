from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test"
)
db = cluster["WoE"]
players = db["players"]


def findUserStats(uid):
    for player in players.find({"_id": uid}):
        return [player['strength'], player['dexterity'], player['intelligence'], player['wisdom'], player['charisma'], player['bodytype']]


def updateMods(user_id):
    player = findUserStats(user_id)
    # сила
    print(player[0])
    if int(player[0]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -5}})
    elif int(player[0]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -4}})
    elif int(player[0]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -3}})
    elif int(player[0]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -2}})
    elif int(player[0]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -1}})
    elif int(player[0]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": 0}})
    elif int(player[0]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +1}})
    elif int(player[0]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +2}})
    elif int(player[0]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +3}})
    elif int(player[0]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +4}})
    elif int(player[0]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +5}})
    # ловкость
    if int(player[1]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -5}})
    elif int(player[1]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -4}})
    elif int(player[1]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -3}})
    elif int(player[1]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -2}})
    elif int(player[1]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -1}})
    elif int(player[1]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": 0}})
    elif int(player[1]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +1}})
    elif int(player[1]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +2}})
    elif int(player[1]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +3}})
    elif int(player[1]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +4}})
    elif int(player[1]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +5}})
    # интеллект
    if int(player[2]) == 1:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": -5}})
    elif int(player[2]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": -4}})
    elif int(player[2]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": -3}})
    elif int(player[2]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": -2}})
    elif int(player[2]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": -1}})
    elif int(player[2]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": 0}})
    elif int(player[2]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": +1}})
    elif int(player[2]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": +2}})
    elif int(player[2]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": +3}})
    elif int(player[2]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": +4}})
    elif int(player[2]) == 20:
        players.update_one({"_id": user_id}, {
                           "$set": {"mod_intelligence": +5}})
    # мудрость
    if int(player[3]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -5}})
    elif int(player[3]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -4}})
    elif int(player[3]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -3}})
    elif int(player[3]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -2}})
    elif int(player[3]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -1}})
    elif int(player[3]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": 0}})
    elif int(player[3]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +1}})
    elif int(player[3]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +2}})
    elif int(player[3]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +3}})
    elif int(player[3]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +4}})
    elif int(player[3]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +5}})
    # харизима
    if int(player[4]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -5}})
    elif int(player[4]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -4}})
    elif int(player[4]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -3}})
    elif int(player[4]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -2}})
    elif int(player[4]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -1}})
    elif int(player[4]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": 0}})
    elif int(player[4]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +1}})
    elif int(player[4]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +2}})
    elif int(player[4]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +3}})
    elif int(player[4]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +4}})
    elif int(player[4]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +5}})
    # телосложение
    if int(player[5]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -5}})
    elif int(player[5]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -4}})
    elif int(player[5]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -3}})
    elif int(player[5]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -2}})
    elif int(player[5]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -1}})
    elif int(player[5]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": 0}})
    elif int(player[5]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +1}})
    elif int(player[5]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +2}})
    elif int(player[5]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +3}})
    elif int(player[5]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +4}})
    elif int(player[5]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +5}})
