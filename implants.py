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
implants = db["implants"]

class Implants:

    def __init__(self, uid):
        self.uid = uid

    def setupPorts(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        imp = getter[0]

        if imp == "Кибераудио":
            implants.update_one({"name": getter[1]}, {
                "$set": {"audio": getter[0]}})
        elif imp == "Нейролинк":
            implants.update_one({"name": getter[1]}, {
                "$set": {"neural": getter[0]}})
        elif imp == "Правый киберглаз":
            implants.update_one({"name": getter[1]}, {
                "$set": {"right_eye": getter[0]}})
        elif imp == "Левый киберглаз":
            implants.update_one({"name": getter[1]}, {
                "$set": {"left_eye": getter[0]}})
        elif imp == "Правая киберрука":
            implants.update_one({"name": getter[1]}, {
                "$set": {"right_arm": getter[0]}})
        elif imp == "Левая киберрука":
            implants.update_one({"name": getter[1]}, {
                "$set": {"left_arm": getter[0]}})
        elif imp == "Правая кибернога":
            implants.update_one({"name": getter[1]}, {
                "$set": {"right_leg": getter[0]}})
        elif imp == "Левая кибернога":
            implants.update_one({"name": getter[1]}, {
                "$set": {"left_leg": getter[0]}})
