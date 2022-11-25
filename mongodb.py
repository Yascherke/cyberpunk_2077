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
weapons = db["weapons"]
armor = db["armor"]
wtypes = db["wtypes"]

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
        return [player['weapon'], player['armor'], player['sp']]

    def backpack(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['slot1'], player['slot2'], player['slot3'], player['slot4'], player['slot5'], player['slot6'], player['slot7'], player['slot8'], player['slot9'], player['slot10']]

    def money(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return player['money']

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
        return [player['ammo'], player['rocket_ammo']]

    def magazine(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['magazine'], player['max_magazine']]

    def dbSkills(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['traits_db'], player['implants_db'], player['programs_db']]

    def moneyByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return player['money']

    def generalByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [player['name'], player['hero_class'], player['rank'], player['rank_exp'], player['car'], player['home']]

    def backpackByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [player['slot1'], player['slot2'], player['slot3'], player['slot4'], player['slot5'], player['slot6'], player['slot7'], player['slot8'], player['slot9'], player['slot10']]

    def weapon(self, name):
        for weapon in weapons.find({"name": name}):
            print('Done')
        return [weapon['_id'], weapon['name'], weapon['type']]

    def armor(self, name):
        for arm in armor.find({"name": name}):
            print('Done')
        return [arm['_id'], arm['name'], arm['sp'], arm['price']]

    def wtype(self, type):
        for wtype in wtypes.find({"_id": type}):
            print('Done')
        return [wtype['_id'], wtype['name'], wtype['wp_skill'], wtype['damage'], wtype['magazine'], wtype['type'], wtype['alt'], wtype['prop'], wtype['grip'], wtype['price']]

    def ammoByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [player['ammo'], player['rocket_ammo']]