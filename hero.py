from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint
from statistics import mean


class Hero(StatesGroup):

    # Характеристики
    def getStats():
        def roll():
            stat = []
            n = 0
            while n != 3:
                n += 1
                stat.append(randint(1, 8))

            stat = max(stat)
            return stat

        intelligence = roll()
        reaction = roll()
        dexterity = roll()
        technics = roll()
        charisma = roll()
        will = roll()
        luck = roll()
        speed = roll()
        bodytype = roll()
        empathy = roll()

        max_hp = 10 + (5 * (round(mean([bodytype, will]))))
        hp = max_hp
        severe_injury = round(max_hp / 2)
        die_dice = round(max_hp / 5)
        humanity = empathy * 10

        return [
            intelligence, 
            reaction, 
            dexterity, 
            technics, 
            charisma,
            will,
            luck,
            speed,
            bodytype,
            empathy,
            max_hp,
            hp,
            severe_injury,
            die_dice,
            humanity
            ]

    # Основная информация
    hero_class = 0
    rank = 0
    rank_exp = 0

    car = 0
    home = 0

    # Экипировка
    first_weapon = 0
    second_weapon = 0

    pistol_magazine = 0
    hpistol_magazine = 0
    shpistol_magazine = 0
    shotgun_magazine = 0
    rifle_magazine = 0
    arrow_magazine = 0
    granade_magazine = 0
    rocket_magazine = 0

    pistol_ammo = 0
    hpistol_ammo = 0
    shpistol_ammo = 0
    shotgun_ammo = 0
    rifle_ammo = 0
    arrow_ammo = 0
    granade_ammo = 0
    rocket_ammo = 0

    head_armor = 0
    body_armor = 0
    head_stat = 0
    body_stat = 0

    # Карманы
    slot1 = 0
    slot2 = 0
    slot3 = 0
    slot4 = 0
    slot5 = 0
    slot6 = 0
    slot7 = 0
    slot8 = 0
    slot9 = 0
    slot10 = 0

    # Дополнительная информация
    money = 0
    tokens = 0

    gang = 0
    corp = 0

    admin = False
    gm = False
    status = 0

    mission = 0
    mission_rank = 0
    progress = 0
    mission_count = 0

    # Способности
    traits_db = []
    implants_db = []
    programs_db = []

    traits = []
    implants = []
    programs = []

    role_skill = 0
    rs_rank = 0

    name = State()
