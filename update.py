from pymongo import MongoClient
from mongodb import Finder

cluster = MongoClient(
    "mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test"
)
db = cluster["WoE"]
players = db["players"]
ranks = db["rank"]

def updateRank(uid):
        finder = Finder(uid)
        gen_info = finder.generalInfo()
        if gen_info[3] >= 250 and gen_info[3] < 500:
            players.update_one({"_id": uid}, {"$set": {"rank": 1}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            players.update_one({"_id": uid}, {"$set": {"rank": 2}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            players.update_one({"_id": uid}, {"$set": {"rank": 3}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            players.update_one({"_id": uid}, {"$set": {"rank": 4}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            players.update_one({"_id": uid}, {"$set": {"rank": 5}})
        if gen_info[3] >= 8000 and gen_info[3] < 16000:
            players.update_one({"_id": uid}, {"$set": {"rank": 6}})
        if gen_info[3] >= 16000 and gen_info[3] < 32000:
            players.update_one({"_id": uid}, {"$set": {"rank": 7}})
        if gen_info[3] >= 32000 and gen_info[3] < 64000:
            players.update_one({"_id": uid}, {"$set": {"rank": 8}})      
        if gen_info[3] >= 64000 and gen_info[3] < 128000:
            players.update_one({"_id": uid}, {"$set": {"rank": 9}})
        if gen_info[3] >= 128000:
            players.update_one({"_id": uid}, {"$set": {"rank": 10}})
        
        