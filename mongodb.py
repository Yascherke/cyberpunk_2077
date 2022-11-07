from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test"
)
db = cluster["WoE"]
players = db["players"]


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
        return [player['name'], player['hero_class'], player['rank'], player['rank_exp']]

    def hpInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['max_hp'], player['hp'], player['severe_injury'], player['die_dice']]

    def equipment(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['first_weapon'], player['second_weapon'], player['head_armor'], player['body_armor']]

    def backpack(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['slot1'], player['slot2'], player['slot3'], player['slot4'], player['slot5'], player['slot6'], player['slot7'], player['slot8']]

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
        return [player['admin'], player['gm'], player['title']]

    def skills(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['traits'], player['implants']]
