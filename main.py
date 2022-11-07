import asyncio
from cgitb import text
import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pymongo import MongoClient
from aiogram.utils import executor

from hero import Hero as hero
from mongodb import Finder
import markups as nav

logging.basicConfig(level=logging.INFO)

API_TOKEN = "5667925194:AAErD4AwaG_4oRtPWX68Ar3rr8Qs-6uRCW8"
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
                    "intelligence": hero.intelligence,
                    "reaction": hero.reaction,
                    "dexterity": hero.dexterity,
                    "technics": hero.technics,
                    "charisma": hero.charisma,
                    "will": hero.will,
                    "luck": hero.luck,
                    "speed": hero.speed,
                    "bodytype": hero.bodytype,
                    "empathy": hero.empathy,

                    "hero_class": hero.hero_class,

                    "max_hp": hero.max_hp,
                    "hp": hero.hp,
                    "severe_injury": hero.severe_injury,
                    "die_dice": hero.die_dice,

                    "rank": hero.rank,
                    "rank_exp": hero.rank_exp,


                    "first_weapon": hero.first_weapon,
                    "second_weapon": hero.second_weapon,
                    "head_armor": hero.head_armor,
                    "body_armor": hero.body_armor,

                    "slot1": hero.slot1,
                    "slot2": hero.slot2,
                    "slot3": hero.slot3,
                    "slot4": hero.slot4,
                    "slot5": hero.slot5,
                    "slot6": hero.slot6,
                    "slot7": hero.slot7,
                    "slot8": hero.slot8,

                    "money": hero.money,
                    "tokens": hero.tokens,

                    "gang": hero.gang,
                    "corp": hero.corp,

                    "mission": hero.mission,
                    "mission_rank": hero.mission_rank,
                    "progress": hero.progress,
                    "mission_count": hero.mission_count,

                    "traits": hero.traits,
                    "implants": hero.implants,

                    "admin": hero.admin,
                    "gm": hero.gm,
                })

                await state.finish()
            await asyncio.sleep(1)
            await message.answer(f'Удачной игры!')
    else:
        await bot.send_message(message.chat.id, "У вас уже есть персонаж!")


@dp.message_handler()
async def cmd_prof(message: types.Message):
    user_id = message.from_user.id
    finder = Finder(user_id)
    gen_info = finder.generalInfo()
    money = finder.money()
    stats = finder.stats()
    hp = finder.hpInfo()
    skills = finder.skills()
    other = finder.otherInfo()

    def myStats():
        text = f"""
-----------------------------------------
        Характеристики

Интеллект: {stats[0]} 
Реакция: {stats[1]}
Ловкость: {stats[2]} 
Техника: {stats[3]} 
Харизма: {stats[4]} 
Воля: {stats[5]} 
Удача: {stats[6]} 
Скорость: {stats[7]} 
Телосложение: {stats[8]}
Эмпатия: {stats[9]} 

-----------------------------------------
"""
        return text

    if message.text == 'Профиль' or message.text == 'Вернуться назад':
        await message.delete()
        await message.answer(f"""
-----------------------------------------
{gen_info[1]} {gen_info[0]}

Известность: {gen_info[2]}
Очки известности: {gen_info[3]}

Здоровье: {hp[1]} из {hp[0]}
Тяжёлое ранение: {hp[2]}
Испытание смерти: {hp[3]}

Корпораия: {other[1]}
Банда: {stats[0]} 

-----------------------------------------
            Кошелёк

Евродоллары: {money[0]}
Токены: {money[1]}

-----------------------------------------
""", reply_markup=nav.profileMenu)

    if message.text == 'Характеристики':
        await message.delete()
        await message.answer(myStats(), reply_markup=nav.back)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
