from pymongo import MongoClient
from mongodb import Finder
import d20
import collections


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

class Admin:

    def __init__(self, uid):
        self.uid = uid

    def giveExp(self, msg):
        find = Finder(self.uid)
        getter = msg.replace(' для ', ',').split(',')
        role_id = find.getIdByName(getter[1])
        status = find.skills()
        nr = find.getNRunner()

        dice = d20.roll(getter[0])
        reward = dice.total

        if status[4] == "Рокербой":
            rockerboys.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Соло":
            solos.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Нетраннер":
            netrunners.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Техник":
            techs.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Медтехник":
            reapers.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Медиа":
            medias.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Законник":
            police.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Экзек":
            ekzeks.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Фиксер":
            fixer.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
        if status[4] == "Кочевник":
            nomads.update_one({"_id": role_id}, {
                    "$set": {"exp": nr[3] + reward}})
            return reward
