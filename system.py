from pymongo import MongoClient

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
    return [skill['name'], skill['lvl'], skill['base'], skill['desc']]
    
    
    