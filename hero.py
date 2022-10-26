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
    mission_rank = 'F'
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

    # def get_mod(self):
    #     self.mod_strength = 0
    #     self.mod_dexterity = 0
    #     self.mod_intelligence = 0
    #     self.mod_wisdom = 0
    #     self.mod_charisma = 0
    #     self.mod_bodytype = 0

    #     return [self.mod_strength, self.mod_dexterity, self.mod_intelligence, self.mod_wisdom, self.mod_charisma, self.mod_bodytype, self.mod_points]

    # def get_sp(self):
    #     self.sp_strength = 0
    #     self.sp_dexterity = 0
    #     self.sp_intelligence = 0
    #     self.sp_wisdom = 0
    #     self.sp_charisma = 0
    #     self.sp_bodytype = 0

    #     return [self.sp_strength, self.sp_dexterity, self.sp_intelligence, self.sp_wisdom, self.sp_charisma, self.sp_bodytype, self.sp_points]

    # def get_main_info(self):
    #     self.hero_class = 'Простолюдин'
    #     self.spec = 'Отсутствует'
    #     self.race = 'Человек'

    #     self.level = 1
    #     self.exp = 0

    #     self.max_hp = 0
    #     self.hp = 0
    #     self.time_hp = 0
    #     self.dice_hp = 0

    #     self.ac = 10
    #     self.mastery = 2

    #     self.base_char = 'Отсутствует'

    #     return [self.hero_class, self.spec, self.race, self.level, self.exp, self.max_hp, self.hp, self.time_hp, self.dice_hp, self.ac, self.mastery, self.base_char]

    # def get_equip(self):
    #     self.main_hand = 0
    #     self.off_hand = 0
    #     self.armor = 0

    #     self.amulet = 0
    #     self.ring1 = 0
    #     self.ring2 = 0
    #     self.accessory1 = 0
    #     self.accessory2 = 0

    #     return [self.main_hand, self.off_hand, self.armor, self.amulet, self.ring1, self.ring2, self.accessory1, self.accessory2]

    # def get_backpack(self):
    #     self.slot1 = 0
    #     self.slot2 = 0
    #     self.slot3 = 0
    #     self.slot4 = 0
    #     self.slot5 = 0
    #     self.slot6 = 0
    #     self.slot7 = 0
    #     self.slot8 = 0

    #     return [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6, self.slot7, self.slot8]

    # def get_other(self):
    #     self.copper_coin = 0
    #     self.silver_coin = 0
    #     self.gold_coin = 0
    #     self.platinum_coin = 0

    #     self.party = 0
    #     self.guild = 0
    #     self.guild_title = 0

    #     self.location = 0

    #     self.admin = False
    #     self.gm = False

    #     self.mission = 0
    #     self.progress = 0
    #     self.mission_count = 0

    #     self.title = 0
    #     self.status = 0

    #     return [self.copper_coin, self.silver_coin, self.gold_coin, self.platinum_coin, self.party, self.guild, self.guild_title, self.status]
