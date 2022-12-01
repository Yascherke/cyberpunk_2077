from pymongo import MongoClient
from mongodb import Finder
import d20

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
programs = db["programs"]

class Interface:

    def __init__(self, uid):
        self.uid = uid

    def checkAction(self):
        find = Finder(self.uid)
        nr = find.getNRunner()

        roll = d20.roll("1d10 +"+str(nr[2]))

        return roll

    def buyProgram(uid, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(uid)
        player = find.getIdByName(getter[1])
        finder = Finder(player)
        money = finder.money()
        deka = finder.nrPrograms()

        try:
            getProgram = finder.getProgram(getter[0])
        except:
            return False

        count = 0
        for item in deka:
            if item == 0 and int(money) >= getProgram[6]:
                netrunners.update_one({"_id": player}, {
                    "$set": {"program"+str(count+1): getProgram[0]}})
                players.update_one({"_id": player}, {
                    "$set": {"money": int(money) - int(getProgram[6])}})
                return True
            else:
                if count < 11:
                    count += 1
                else:
                    return False

    def updateAction(self):
        finder = Finder(self.uid)
        action = finder.getNRunner()
        
        if action[2] >= 1 and action[2] <= 3:
            netrunners.update_one({"_id": self.uid}, {
                "$set": {"action": 2}})
        elif action[2] >= 4 and action[2] <= 6:
            netrunners.update_one({"_id": self.uid}, {
                "$set": {"action": 3}})
        elif action[2] >= 7 and action[2] <= 9:
            netrunners.update_one({"_id": self.uid}, {
                "$set": {"action": 4}})
        else:
            netrunners.update_one({"_id": self.uid}, {
                "$set": {"action": 5}})
            
    def lvlUp(self):
        finder = Finder(self.uid)
        gen_info = finder.getNRunner()
        
        if gen_info[3] < 250:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 9}})
        if gen_info[3] >= 30000:
            players.update_one({"_id": self.uid}, {"$set": {"rank": 10}})