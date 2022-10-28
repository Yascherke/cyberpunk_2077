from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profileMenu = ReplyKeyboardMarkup(resize_keyboard=True)
profileBack = ReplyKeyboardMarkup(resize_keyboard=True)
btnStats = KeyboardButton(text="Характеристики")
btnEquip = KeyboardButton(text="Экипировка")
btnBp = KeyboardButton(text="Рюкзак")


profileMenu.add(btnStats, btnEquip, btnBp)
