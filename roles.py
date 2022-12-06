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


class Role:

    def __init__(self, uid):
        self.uid = uid

    def rocker(self):
        finder = Finder(self.uid)
        gen_info = finder.rockerboy()
        
        if gen_info[3] < 250:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            rockerboys.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
    
    def solo(self):
        finder = Finder(self.uid)
        gen_info = finder.solo()
        
        if gen_info[3] < 250:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            solos.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
    
    def media(self):
        finder = Finder(self.uid)
        gen_info = finder.media()
        
        if gen_info[3] < 250:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            medias.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
    
    def police(self):
        finder = Finder(self.uid)
        gen_info = finder.police()
        
        if gen_info[3] < 250:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            police.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
    
    def fixer(self):
        finder = Finder(self.uid)
        gen_info = finder.fixer()
        
        if gen_info[3] < 250:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            fixer.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
    
    def nomad(self):
        finder = Finder(self.uid)
        gen_info = finder.nomad()
        
        if gen_info[3] < 250:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            nomads.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
    
    def ekzek(self):
        finder = Finder(self.uid)
        gen_info = finder.ekzek()
        
        if gen_info[3] < 250:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            ekzeks.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
        
    def reaper(self):
        finder = Finder(self.uid)
        gen_info = finder.reaper()
        
        if gen_info[3] < 250:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            reapers.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})
    
    def tech(self):
        finder = Finder(self.uid)
        gen_info = finder.tech()
        
        if gen_info[3] < 250:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 1}})
        if gen_info[3] >= 250 and gen_info[3] < 500:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 2}})
        if gen_info[3] >= 500 and gen_info[3] < 1000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 3}})
        if gen_info[3] >= 1000 and gen_info[3] < 2000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 4}})
        if gen_info[3] >= 2000 and gen_info[3] < 4000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 5}})
        if gen_info[3] >= 4000 and gen_info[3] < 8000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 6}})
        if gen_info[3] >= 8000 and gen_info[3] < 10000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 7}})
        if gen_info[3] >= 10000 and gen_info[3] < 15000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 8}})      
        if gen_info[3] >= 15000 and gen_info[3] < 20000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 9}})
        if gen_info[3] >= 30000:
            techs.update_one({"_id": self.uid}, {"$set": {"lvl": 10}})

    def techPoint(self, msg):

        find = Finder(self.uid)
        role = find.tech()

        if role[4] != 0 and msg == "Модернизация":
            techs.update_one({"_id": self.uid}, {"$set": {"modern": role[5] + 1}})
            techs.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Изготовитель":
            techs.update_one({"_id": self.uid}, {"$set": {"crafter": role[6] + 1}})
            techs.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Изобретатель":
            techs.update_one({"_id": self.uid}, {"$set": {"creator": role[7] + 1}})
            techs.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        else:
            False

    def medPoint(self, msg):

        find = Finder(self.uid)
        role = find.reaper()

        if role[4] != 0 and msg == "Хирургия":
            reapers.update_one({"_id": self.uid}, {"$set": {"surgeon": role[5] + 1}})
            reapers.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Фармацевтика":
            reapers.update_one({"_id": self.uid}, {"$set": {"pharmacist": role[6] + 1}})
            reapers.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Изобретатель":
            reapers.update_one({"_id": self.uid}, {"$set": {"Криосистемы": role[7] + 1}})
            reapers.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        else:
            False