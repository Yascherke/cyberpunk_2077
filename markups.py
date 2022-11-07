from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

profileMenu = ReplyKeyboardMarkup(resize_keyboard=True)
profileStats = ReplyKeyboardMarkup(resize_keyboard=True)
back = ReplyKeyboardMarkup(resize_keyboard=True)
btnStats = KeyboardButton(text="Характеристики")
btnEquip = KeyboardButton(text="Экипировка")
btnBp = KeyboardButton(text="Рюкзак")

btnBack = KeyboardButton(text="Вернуться назад")


profileMenu.add(btnStats, btnEquip)
back.add(btnBack)