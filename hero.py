from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint


class Hero(StatesGroup):

    def get_points():
        return randint(65, 85)

    # Характеристики
    strength = 1
    dexterity = 1
    intelligence = 1
    wisdom = 1
    charisma = 1
    bodytype = 1

    points = get_points()

    # Модификатор характеристики
    mod_strength = 0
    mod_dexterity = 0
    mod_intelligence = 0
    mod_wisdom = 0
    mod_charisma = 0
    mod_bodytype = 0

    # Спасброски
    sp_strength = 0
    sp_dexterity = 0
    sp_intelligence = 0
    sp_wisdom = 0
    sp_charisma = 0
    sp_bodytype = 0

    # Основная информация
    hero_class = 0
    spec = 0
    race = 0

    level = 1
    exp = 0
    rank = 'F'

    max_hp = 0
    hp = 0
    time_hp = 0
    dice_hp = 0

    ac = 10
    mastery = 2

    base_char = 'None'

    # Экипировка
    main_hand = 0
    off_hand = 0
    armor = 0

    amulet = 0
    ring1 = 0
    ring2 = 0
    accessory1 = 0
    accessory2 = 0

    # Рюкзак
    slot1 = 0
    slot2 = 0
    slot3 = 0
    slot4 = 0
    slot5 = 0
    slot6 = 0
    slot7 = 0
    slot8 = 0

    # Дополнительная информация
    copper_coin = 0
    silver_coin = 0
    gold_coin = 0
    platinum_coin = 0

    party = 0
    guild = 0
    guild_title = 0

    location = 0

    admin = False
    gm = False

    mission = 0
    mission_rank = 0
    progress = 0
    mission_count = 0

    title = 0
    status = 0

    # Способности
    traits = []
    mana = 0
    max_mana = 0
    cantrips = []
    spells = []

    name = State()