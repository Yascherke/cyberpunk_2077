import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pymongo import MongoClient
from aiogram.utils import executor

from hero import Hero as hero


logging.basicConfig(level=logging.INFO)

API_TOKEN = "5620891819:AAFlR04CBqCnDu74oZLJAkbS8oCWX9SKkTE"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

cluster = MongoClient(
    "mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test"
)
db = cluster["WoE"]
players = db["players"]


def findUserParamByID(uid):
    for player in players.find({"_id": uid}):
        pid = player['_id']
        return pid


def findUserParam(uid):
    for player in players.find({"_id": uid}):
        return [player['strength'], player['dexterity'], player['intelligence'],player['wisdom'],player['charisma'],player['bodytype'] ]


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    uid = message.from_user.id
    p_id = findUserParamByID(uid)
    if p_id is None:
        await hero.name.set()
        await message.answer("Как зовут вашего персонажа")

        @dp.message_handler(state=hero.name)
        async def cmd_name(message: types.Message, state: FSMContext):
            await hero.name.set()

            async with state.proxy() as data:
                data['Name'] = message.text
                uid = message.from_user.id
                name = data['Name']

                players.insert_one({
                    "_id": uid,
                    "name": name,
                    "strength": hero.strength,
                    "dexterity": hero.dexterity,
                    "intelligence": hero.intelligence,
                    "wisdom": hero.wisdom,
                    "charisma": hero.charisma,
                    "bodytype": hero.bodytype,
                    "points": hero.points,

                    "mod_strength": hero.mod_strength,
                    "mod_dexterity": hero.mod_dexterity,
                    "mod_intelligence": hero.mod_intelligence,
                    "mod_wisdom": hero.mod_wisdom,
                    "mod_charisma": hero.mod_charisma,
                    "mod_bodytype": hero.mod_bodytype,

                    "sp_strength": hero.sp_strength,
                    "sp_dexterity": hero.sp_dexterity,
                    "sp_intelligence": hero.sp_intelligence,
                    "sp_wisdom": hero.sp_wisdom,
                    "sp_charisma": hero.sp_charisma,
                    "sp_bodytype": hero.sp_bodytype,

                    "hero_class": hero.hero_class,
                    "spec": hero.spec,
                    "race": hero.race,
                    "level": hero.level,
                    "exp": hero.exp,
                    "max_hp": hero.max_hp,
                    "hp": hero.hp,
                    "time_hp": hero.time_hp,
                    "dice_hp": hero.dice_hp,
                    "ac": hero.ac,
                    "base_char": hero.base_char,
                    "rank": hero.rank,

                    "main_hand": hero.main_hand,
                    "off_hand": hero.off_hand,
                    "armor": hero.armor,
                    "amulet": hero.amulet,
                    "ring1": hero.ring1,
                    "ring2": hero.ring2,
                    "accessory1": hero.accessory1,
                    "accessory2": hero.accessory2,

                    "slot1": hero.slot1,
                    "slot2": hero.slot2,
                    "slot3": hero.slot3,
                    "slot4": hero.slot4,
                    "slot5": hero.slot5,
                    "slot6": hero.slot6,
                    "slot7": hero.slot7,
                    "slot8": hero.slot8,

                    "copper_coin": hero.copper_coin,
                    "silver_coin": hero.silver_coin,
                    "gold_coin": hero.gold_coin,
                    "platinum_coin": hero.platinum_coin,
                    "party": hero.party,
                    "guild": hero.guild,
                    "guild_title": hero.guild_title,
                    "location": hero.location,
                    "title": hero.title,
                    "status": hero.status,
                    "mission": hero.mission,
                    "mission_rank": hero.mission_rank,
                    "progress": hero.progress,
                    "mission_count": hero.mission_count,
                    "traits": hero.traits,
                    "mana": hero.mana,
                    "max_mana": hero.max_mana,
                    "cantrips": hero.cantrips,
                    "spells": hero.spells,

                    "admin": hero.admin,
                    "gm": hero.gm,
                })

                await state.finish()
            await asyncio.sleep(1)
            await message.answer(f'Удачной игры!')
    else:
        await bot.send_message(message.chat.id, "У вас уже есть персонаж!")


@dp.message_handler(commands=['update'])
async def cmd_mod(message: types.Message):
    user_id = message.from_user.id
    player = findUserParam(user_id)
    # сила
    if int(player[0]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -5}})
    elif int(player[0]) == 2 or int(player[0]) == 3 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -4}})
    elif int(player[0]) == 4 or int(player[0]) == 5 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -3}})
    elif int(player[0]) == 6 or int(player[0]) == 7 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -2}})
    elif int(player[0]) == 8 or int(player[0]) == 9 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": -1}})
    elif int(player[0]) == 10 or int(player[0]) == 11 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": 0}})
    elif int(player[0]) == 12 or int(player[0]) == 13 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +1}})
    elif int(player[0]) == 14 or int(player[0]) == 15 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +2}})
    elif int(player[0]) == 16 or int(player[0]) == 17 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +3}})
    elif int(player[0]) == 18 or int(player[0]) == 19 :
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +4}})
    elif int(player[0]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_strength": +5}})
    # уклонение
    if int(player[1]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -5}})
    elif int(player[1]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -4}})
    elif int(player[1]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -3}})
    elif int(player[1]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -2}})
    elif int(player[1]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": -1}})
    elif int(player[1]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": 0}})
    elif int(player[1]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +1}})
    elif int(player[1]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +2}})
    elif int(player[1]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +3}})
    elif int(player[1]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +4}})
    elif int(player[1]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_dexterity": +5}})
    # интеллект
    if int(player[2]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": -5}})
    elif int(player[2]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": -4}})
    elif int(player[2]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": -3}})
    elif int(player[2]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": -2}})
    elif int(player[2]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": -1}})
    elif int(player[2]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": 0}})
    elif int(player[2]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": +1}})
    elif int(player[2]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": +2}})
    elif int(player[2]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": +3}})
    elif int(player[2]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": +4}})
    elif int(player[2]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_intelligence": +5}})
    # мудрость
    if int(player[3]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -5}})
    elif int(player[3]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -4}})
    elif int(player[3]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -3}})
    elif int(player[3]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -2}})
    elif int(player[3]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": -1}})
    elif int(player[3]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": 0}})
    elif int(player[3]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +1}})
    elif int(player[3]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +2}})
    elif int(player[3]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +3}})
    elif int(player[3]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +4}})
    elif int(player[3]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_wisdom": +5}})
    # харизима
    if int(player[4]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -5}})
    elif int(player[4]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -4}})
    elif int(player[4]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -3}})
    elif int(player[4]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -2}})
    elif int(player[4]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": -1}})
    elif int(player[4]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": 0}})
    elif int(player[4]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +1}})
    elif int(player[4]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +2}})
    elif int(player[4]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +3}})
    elif int(player[4]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +4}})
    elif int(player[4]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_charisma": +5}})
    # телосложение
    if int(player[5]) == 1:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -5}})
    elif int(player[5]) == 2 or int(player[0]) == 3:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -4}})
    elif int(player[5]) == 4 or int(player[0]) == 5:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -3}})
    elif int(player[5]) == 6 or int(player[0]) == 7:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -2}})
    elif int(player[5]) == 8 or int(player[0]) == 9:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": -1}})
    elif int(player[5]) == 10 or int(player[0]) == 11:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": 0}})
    elif int(player[5]) == 12 or int(player[0]) == 13:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +1}})
    elif int(player[5]) == 14 or int(player[0]) == 15:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +2}})
    elif int(player[5]) == 16 or int(player[0]) == 17:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +3}})
    elif int(player[5]) == 18 or int(player[0]) == 19:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +4}})
    elif int(player[5]) == 20:
        players.update_one({"_id": user_id}, {"$set": {"mod_bodytype": +5}})




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
