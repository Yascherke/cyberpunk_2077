from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profileMenu = ReplyKeyboardMarkup(resize_keyboard=True)
profileStats = ReplyKeyboardMarkup(resize_keyboard=True)
back = ReplyKeyboardMarkup(resize_keyboard=True)
btnStats = KeyboardButton(text="Характеристики")
btnEquip = KeyboardButton(text="Экипировка")
btnBp = KeyboardButton(text="Имущество")

btnBack = KeyboardButton(text="Вернуться назад")


profileMenu.add(btnStats, btnEquip, btnBp)
back.add(btnBack)

