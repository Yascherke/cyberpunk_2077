import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pymongo import MongoClient
from aiogram.utils import executor
import re

from hero import Hero as hero
from mongodb import Finder
from view import View
import markups as nav
from system import getRole, getSkill

from ws import keep_alive

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
roles = db["class"]
wtypes = db["wtypes"]
weapons = db["weapons"]
armor = db["armor"]
skills = db["skills"]


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
                stats = hero.getStats()
                money = hero.moneyRoll()
                view = View(uid)

                players.insert_one({
                    "_id": uid,
                    "name": name,
                    "intelligence": stats[0],
                    "reaction": stats[1],
                    "dexterity": stats[2],
                    "technics": stats[3],
                    "charisma": stats[4],
                    "will": stats[5],
                    "luck": stats[6],
                    "speed": stats[7],
                    "bodytype": stats[8],
                    "empathy": stats[9],

                    "hero_class": hero.hero_class,
                    "car": hero.car,
                    "home": hero.home,

                    "max_hp": stats[10],
                    "hp": stats[11],
                    "severe_injury": stats[12],
                    "die_dice": stats[13],

                    "rank": hero.rank,
                    "rank_exp": hero.rank_exp,

                    "first_weapon": hero.first_weapon,
                    "second_weapon": hero.second_weapon,

                    "head_armor": hero.head_armor,
                    "body_armor": hero.body_armor,
                    "head_stat": hero.head_stat,
                    "body_stat": hero.body_stat,

                    "money": money,
                    "tokens": hero.tokens,

                    "gang": hero.gang,
                    "corp": hero.corp,

                    "mission": hero.mission,
                    "mission_rank": hero.mission_rank,
                    "progress": hero.progress,
                    "mission_count": hero.mission_count,

                    "traits_db": hero.traits,
                    "implants_db": hero.implants,
                    "programs_db": hero.programs,

                    "traits": hero.traits,
                    "implants": hero.implants,
                    "programs": hero.programs,

                    "admin": hero.admin,
                    "gm": hero.gm,
                    "humanity": stats[14],
                    "status": hero.status,

                    "role_skill": hero.role_skill,
                    "rs_rank": hero.rs_rank,

                    "slot1": hero.slot1,
                    "slot2": hero.slot2,
                    "slot3": hero.slot3,
                    "slot4": hero.slot4,
                    "slot5": hero.slot5,
                    "slot6": hero.slot6,
                    "slot7": hero.slot7,
                    "slot8": hero.slot8,
                    "slot9": hero.slot9,
                    "slot10": hero.slot10,

                    "pistol_magazine": hero.pistol_magazine,
                    "hpistol_magazine": hero.hpistol_magazine,
                    "shpistol_magazine": hero.shpistol_magazine,
                    "shotgun_magazine": hero.shotgun_magazine,
                    "rifle_magazine": hero.rifle_magazine,
                    "arrow_magazine": hero.arrow_magazine,
                    "granade_magazine": hero.granade_magazine,
                    "rocket_magazine": hero.rocket_magazine,

                    "pistol_ammo": hero.pistol_ammo,
                    "hpistol_ammo": hero.hpistol_ammo,
                    "shpistol_ammo": hero.shpistol_ammo,
                    "shotgun_ammo": hero.shotgun_ammo,
                    "rifle_ammo": hero.rifle_ammo,
                    "arrow_ammo": hero.arrow_ammo,
                    "granade_ammo": hero.granade_ammo,
                    "rocket_ammo": hero.rocket_ammo,
                })

                await state.finish()
            await asyncio.sleep(1)
            await message.answer(f'Удачной игры!')
            await message.answer(view.myProfile(), reply_markup=nav.profileMenu)

    else:
        await bot.send_message(message.chat.id, "У вас уже есть персонаж!")


@dp.message_handler(commands=['роль'])
async def cmd_start(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    player_role = getRole(getter)
    p_name = str(getter[1])
    finder = Finder(uid)
    status = finder.status()
    if status[0] == True:
        players.update_one({"name": p_name}, {
                           "$set": {"hero_class": player_role}})
        await message.answer("Роль выдана")
    else:
        await message.answer("У вас недостаточно прав.")


@dp.message_handler(commands=['выдать'])
async def cmd_start(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    rep = {" для ": ",", " на ": ","}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    msg = pattern.sub(lambda m: rep[re.escape(m.group(0))], msg)
    getter = msg.replace(',', ',').split(',')
    name = getter[0]
    perk = getSkill(name)
    p_name = str(getter[2])
    finder = Finder(uid)
    status = finder.status()
    if status[0] == True:
        players.update_one({"name": p_name}, {
                           "$push": {"traits": {"name": perk[0], "lvl": int(getter[1]), "base": perk[1]}}})
        await message.answer("Навык выдан")
    else:
        await message.answer("У вас недостаточно прав.")


@dp.message_handler(commands=['навык'])
async def cmd_start(message: types.Message):
    msg = message.get_args()
    perk = getSkill(msg)
    await message.answer(f"""
Навык: {perk[0]}

Характеристика: {perk[1]}

Описание: {perk[2]}
    """)


@dp.message_handler(commands=['get'])
async def cmd_start(message: types.Message):
    pass

@dp.message_handler()
async def cmd_prof(message: types.Message):
    user_id = message.from_user.id
    view = View(user_id)

    if message.text == 'Профиль' or message.text == 'Вернуться назад':
        await message.delete()

        await message.answer(view.myProfile(), reply_markup=nav.profileMenu)

    if message.text == 'Характеристики':
        await message.delete()
        await message.answer(view.myStats(), reply_markup=nav.back)

    if message.text == 'Имущество':
        await message.delete()
        await message.answer(view.myProperty(), reply_markup=nav.back)

    if message.text == 'Экипировка':
        await message.delete()
        await message.answer(view.myEquip(), reply_markup=nav.back)
        
    if message.text == 'Навыки':
        await message.delete()
        await message.answer(view.mySkills(), reply_markup=nav.back)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
