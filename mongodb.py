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
        return [player['strength'], player['dexterity'], player['intelligence'], player['wisdom'], player['charisma'], player['bodytype'], player['points']]

    def modStats(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['mod_strength'], player['mod_dexterity'], player['mod_intelligence'], player['mod_wisdom'], player['mod_charisma'], player['mod_bodytype']]

    def generalInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['name'], player['hero_class'], player['spec'], player['race'], player['level'], player['exp'], player['rank'], player['ac'], player['mastery'], player['base_char']]

    def hpInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['max_hp'], player['hp'], player['time_hp'], player['dice_hp']]

    def equipment(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['main_hand'], player['off_hand'], player['armor'], player['amulet'], player['ring1'], player['ring2'], player['accessory1'], player['accessory2']]

    def backpack(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['slot1'], player['slot2'], player['slot3'], player['slot4'], player['slot5'], player['slot6'], player['slot7'], player['slot8']]

    def money(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['copper_coin'], player['silver_coin'], player['gold_coin'], player['platinum_coin']]

    def otherInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['party'], player['guild'], player['guild_title'], player['location']]

    def missions(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['mission'], player['mission_rank'], player['progress'], player['mission_count']]

    def status(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['location'], player['admin'], player['gm'], player['title'], player['status']]

    def magic(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['mana'], player['max_mana'], player['traits'], player['cantrips'], player['spells']]
