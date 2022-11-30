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

from system import getRole, getSkill, send_money, send_exp, bank, giveItem, equip_wp, equip_armor, output, buyArmor, buyWp, buy_ammo, send_ammo
from fight import initiate, shot, reloading, getDamage, hit, autoshot, enemyHit, enemyShot

from ws import keep_alive

keep_alive()
logging.basicConfig(level=logging.INFO)

API_TOKEN = "5667925194:AAErD4AwaG_4oRtPWX68Ar3rr8Qs-6uRCW8"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

cluster = MongoClient(
"mongodb+srv://Nere:0662@woe.vj1q67r.mongodb.net/test&ssl=true&ssl_cert_reqs=CERT_NONE", connect=False)

db = cluster["WoE"]
players = db["players"]
roles = db["class"]
wtypes = db["wtypes"]
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

                    "weapon": hero.weapon,

                    "armor": hero.armor,
                    "sp": hero.sp,

                    "money": money,

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

                    "trauma": hero.trauma,

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

                    "magazine": hero.magazine,
                    "max_magazine": hero.max_magazine,

                    "ammo": hero.ammo,
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
    find = Finder(uid)
    p_name = str(getter[1])
    pid = find.getIdByName(p_name)
    status = find.status()
    if status[0] == True:
        players.update_one({"name": p_name}, {
                           "$set": {"hero_class": player_role}})

        if getter[0] == "Рокебой":
            rockerboys.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Харизма",
                "lvl": 1,
                "exp": 0,
            })

        if getter[0] == "Соло":
            solos.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Боевое чутьё",
                "lvl": 1,
                "exp": 0,
            })

        if getter[0] == "Нетраннер":
            netrunners.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Интерфейс",
                "lvl": 1,
                "exp": 0,
                "action": 2,
                "deka": "Отсутствует",
                "program1": 0,
                "program2": 0,
                "program3": 0,
                "program4": 0,
                "program5": 0,
                "program6": 0,
                "program7": 0,
                "program8": 0,
                "program9": 0,
                "program10": 0,
                "program11": 0,
            })

        if getter[0] == "Техник":
            techs.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Мастер",
                "lvl": 1,
                "exp": 0,
                "points": 0,
                "fullmaster": 1,
                "modern": 1,
                "crafter": 1,
                "creator": 1,
            })

        if getter[0] == "Рипер":
            reapers.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Медицина",
                "lvl": 1,
                "exp": 0,
                "points": 0,
                "surgeon": 1,
                "pharmacist": 1,
                "сryo": 1,
            })

        if getter[0] == "Медиа":
            medias.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Убедительность",
                "lvl": 1,
                "exp": 0,
            })

        if getter[0] == "Экзек":
            ekzeks.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Соло",
                "lvl": 1,
                "exp": 0,
                "slave1": 0,
                "slave2": 0,
                "slave3": 0,

            })

        if getter[0] == "Законник":
            police.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Подкрепление",
                "lvl": 1,
                "exp": 0,
            })

        if getter[0] == "Фиксер":
            fixer.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Делец",
                "lvl": 1,
                "exp": 0,
            })

        if getter[0] == "Кочевник":
            nomads.insert_one({
                "_id": pid,
                "player": getter[1],
                "name": "Мото",
                "lvl": 1,
                "exp": 0,
                "car1": 0,
                "car2": 0,
                "car3": 0,
                "car4": 0,

                "car_info1": [],
                "car_info2": [],
                "car_info3": [],
                "car_info4": [],
            })

        await message.answer("Роль выдана")
        await message.delete()
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
        await message.delete()
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


@dp.message_handler(commands=['перечислить'])
async def sendmon(message: types.Message):
    uid = message.from_user.id
    find = Finder(uid)
    userMon = find.money()
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    money = int(getter[0])
    if userMon[0] >= money:
        send_money(uid, msg)
        await message.answer("Перевод проведен успешно")
    else:
        await message.answer("У вас недостаточно эдди")


@dp.message_handler(commands=['отдать'])
async def give(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    find = Finder(uid)
    getter = msg.replace(' для ', ',').split(',')
    slot = int(getter[0])
    owner = find.backpack()
    for_key = slot-1
    owner_item = owner[for_key]
    func = giveItem(uid, msg)

    if func is True:
        await message.answer(f"Вы передали {owner_item} в руки {getter[1]}")
    else:
        await message.answer("У вас не вышло")


@dp.message_handler(commands=['известность'])
async def sendfame(message: types.Message):
    uid = message.from_user.id
    find = Finder(uid)
    status = find.status()
    msg = message.get_args()
    if status[0] != False or status[1] != False:
        send_exp(uid, msg)
        await message.answer("Известность повышена")
    else:
        await message.answer("У вас нет прав")


@dp.message_handler(commands=['банк'])
async def bank(message: types.Message):
    uid = message.from_user.id
    find = Finder(uid)
    status = find.status()
    msg = message.get_args()
    if status[0] != False or status[1] != False:
        bank_gm(uid, msg)
        await message.answer("Средства перечислены")
    else:
        await message.answer("У вас нет прав")


@dp.message_handler(commands=['оружие'])
async def equipwp(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    find = Finder(uid)
    slot = int(msg)
    owner = find.backpack()
    for_key = slot-1
    owner_item = owner[for_key]
    func = equip_wp(uid, msg)

    if func is True:
        await message.answer(f"Вы экипировали {owner_item}")
    else:
        await message.answer("Это не оружие")


@dp.message_handler(commands=['броня'])
async def equipwp(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    find = Finder(uid)
    slot = int(msg)
    owner = find.backpack()
    for_key = slot-1
    owner_item = owner[for_key]
    func = equip_armor(uid, msg)

    if func is True:
        await message.answer(f"Вы экипировали {owner_item}")
    else:
        await message.answer("Это не броня")


@dp.message_handler(commands=['снять'])
async def output_eq(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    print(uid, msg)
    func = output(uid, msg)

    if func is True:
        await message.answer(f"Вы избавились от предмета")
    else:
        await message.answer("Слот пуст")


@dp.message_handler(commands=['выстрелить'])
async def cmd_shot(message: types.Message):
    uid = message.from_user.id
    func = shot(uid)

    if await message.answer(f"Вы нанесли {func} урона") != False:
        print("Done")
    else:
        await message.answer(f"У вас не вышло")


@dp.message_handler(commands=['попадание'])
async def cmd_hit(message: types.Message):
    msg = message.get_args()

    await message.answer(f"Попадание: {hit(msg)}")


@dp.message_handler(commands=['инициатива'])
async def cmd_initiate(message: types.Message):
    uid = message.from_user.id

    await message.answer(f"Инициатива: {initiate(uid)}")


@dp.message_handler(commands=['перезарядка'])
async def cmd_reload(message: types.Message):
    uid = message.from_user.id
    func = reloading(uid)

    if func is True:
        await message.answer(f"Вы перезарядили оружие")
    else:
        await message.answer("У вас не вышло")


@dp.message_handler(commands=['урон'])
async def bank(message: types.Message):
    uid = message.from_user.id
    find = Finder(uid)
    msg = message.get_args()
    getDamage(uid, msg)
    await message.answer("Урон вычтен")


@dp.message_handler(commands=['купить_оружие'])
async def cmd_wp(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    func = buyWp(uid, msg)

    if func is True:
        await message.answer(f"Вы купили оружие")
    else:
        await message.answer("У вас не вышло")


@dp.message_handler(commands=['купить_броню'])
async def cmd_armor(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    func = buyArmor(uid, msg)

    if func is True:
        await message.answer(f"Вы купили броню")
    else:
        await message.answer("У вас не вышло")


@dp.message_handler(commands=['купить_патроны'])
async def cmd_wp(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    func = buy_ammo(uid, msg)

    if func is True:
        await message.answer(f"Вы купили патроны")
    else:
        await message.answer("У вас не вышло")


@dp.message_handler(commands=['автоогонь'])
async def cmd_auto(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    func = autoshot(uid, msg)

    if await message.answer(f"Вы нанесли {func} урона") != False:
        print("Done")
    else:
        await message.answer(f"У вас не вышло")


@dp.message_handler(commands=['противник_выстрел'])
async def cmd_enshot(message: types.Message):
    msg = message.get_args()
    func = enemyShot(msg)

    await message.answer(f"Противник нанес {func} урона")

@dp.message_handler(commands=['противник_попадание'])
async def cmd_enhit(message: types.Message):
    msg = message.get_args()
    func = enemyShot(msg)

    await message.answer(f"Попадание противника: {func}")



@dp.message_handler(commands=['дать_патроны'])
async def sendmon(message: types.Message):
    uid = message.from_user.id
    find = Finder(uid)
    ammo = find.ammo()
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    send_ammos = int(getter[0])
    if ammo[0] >= send_ammos:
        send_ammo(uid, msg)
        await message.answer("Перевод проведен успешно")
    else:
        await message.answer("У вас недостаточно эдди")


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
