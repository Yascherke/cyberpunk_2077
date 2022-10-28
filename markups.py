from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profileMenu = ReplyKeyboardMarkup(resize_keyboard=True)
profileStats = ReplyKeyboardMarkup(resize_keyboard=True)
btnStats = KeyboardButton(text="Характеристики")
btnEquip = KeyboardButton(text="Экипировка")
btnBp = KeyboardButton(text="Рюкзак")

btnUpStr = KeyboardButton(text="Улучшить силу")
btnUpDex = KeyboardButton(text="Улучшить ловкость")
btnUpInt = KeyboardButton(text="Улучшить ителлект")
btnUpWis = KeyboardButton(text="Улучшить мудрость")
btnUpChar = KeyboardButton(text="Улучшить харизму")
btnUpBody = KeyboardButton(text="Улучшить телосложение")
btnBack = KeyboardButton(text="Вернуться назад")

profileMenu.add(btnStats, btnEquip, btnBp)
profileStats.add(btnUpStr, btnUpDex, btnUpInt, btnUpWis, btnUpChar, btnUpBody, btnBack)
