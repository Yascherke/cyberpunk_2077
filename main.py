import asyncio
from cgitb import text
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pymongo import MongoClient
from aiogram.utils import executor

from hero import Hero as hero
from update import updateMods


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
    updateMods(user_id)
    await message.answer('Готово')

@dp.message_handler()
async def cmd_prof(message: types.Message):
    user_id = message.from_user.id
    if message.text == 'Профиль':
        await message.delete()
        await message.answer(f"""
-----------------------------------------

-----------------------------------------
""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
