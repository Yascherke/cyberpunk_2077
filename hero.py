from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint


class Hero(StatesGroup):

    def rollstats():
        return randint(1,10)

    # Характеристики
    intelligence = rollstats()
    reaction = rollstats()
    dexterity = rollstats()
    technics = rollstats()
    charisma = rollstats()
    will = rollstats()
    luck = rollstats()
    speed = rollstats()
    bodytype = rollstats()
    empathy  = rollstats()

    # Основная информация
    hero_class = 0
    rank = 0
    rank_exp = 0

    max_hp = 0
    hp = 0
    severe_injury = 0
    die_dice = 0

    # Экипировка
    first_weapon = 0
    second_weapon = 0

    head_armor = 0
    body_armor = 0

    # Карманы
    slot1 = 0
    slot2 = 0
    slot3 = 0
    slot4 = 0
    slot5 = 0
    slot6 = 0
    slot7 = 0
    slot8 = 0

    # Дополнительная информация
    money = 0
    tokens = 0

    gang = 0
    corp = 0

    admin = False
    gm = False

    mission = 0
    mission_rank = 0
    progress = 0
    mission_count = 0

    # Способности
    traits = []
    implants = []

    name = State()