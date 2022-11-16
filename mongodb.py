from pymongo import MongoClient

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

class Finder:

    def __init__(self, uid):
        self.uid = uid

    def stats(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['intelligence'], player['reaction'], player['dexterity'], player['technics'], player['charisma'], player['will'], player['luck'], player['speed'], player['bodytype'], player['empathy']]

    def generalInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['name'], player['hero_class'], player['rank'], player['rank_exp'], player['car'], player['home']]

    def hpInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['max_hp'], player['hp'], player['severe_injury'], player['die_dice']]

    def equipment(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['first_weapon'], player['second_weapon'], player['head_armor'], player['body_armor'], player['head_stat'], player['body_stat']]

    def backpack(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['slot1'], player['slot2'], player['slot3'], player['slot4'], player['slot5'], player['slot6'], player['slot7'], player['slot8'], player['slot9'], player['slot10']]

    def money(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['money'], player['tokens']]

    def otherInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['gang'], player['corp']]

    def missions(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['mission'], player['mission_rank'], player['progress'], player['mission_count']]

    def status(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['admin'], player['gm'], player['status']]

    def skills(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['traits'], player['implants'], player['programs'], player['humanity'], player['status'], player['role_skill'], player['rs_rank']]

    def roles(self, id):
        for role in roles.find({"_id": id}):
            return role["Name"]
    
    def corps(self, id):
        for corp in corps.find({"_id": id}):
            return corp["name"]

    def ranks(self, id):
        for rank in ranks.find({"_id": id}):
            print('Done')
        return [rank['name'], rank['rank_exp'], rank["_id"]]
    
    def cars(self, id):
        for car in cars.find({"_id": id}):
            print('Done')
        return [car['name'], car['cost']]

    def houses(self, id):
        for house in houses.find({"_id": id}):
            print('Done')
        return [house['name'], house['cost']]

    def ammo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['pistol_ammo'], player['hpistol_ammo'], player['shpistol_ammo'], player['shotgun_ammo'], player['rifle_ammo'], player['arrow_ammo'], player['granade_ammo'], player['rocket_ammo']]

    def magazine(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['pistol_magazine'], player['hpistol_magazine'], player['shpistol_magazine'], player['shotgun_magazine'], player['rifle_magazine'], player['arrow_magazine'], player['granade_magazine'], player['rocket_magazine']]

    def dbSkills(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['traits_db'], player['implants_db'], player['programs_db']]

    def moneyByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [player['money'], player['tokens']]

    def generalByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [player['name'], player['hero_class'], player['rank'], player['rank_exp'], player['car'], player['home']]

    def backpackByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [player['slot1'], player['slot2'], player['slot3'], player['slot4'], player['slot5'], player['slot6'], player['slot7'], player['slot8'], player['slot9'], player['slot10']]