from pymongo import MongoClient
from mongodb import Finder
import d20

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
lvls = db["lvls"]


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
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            netrunners.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            netrunners.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True