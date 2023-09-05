from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

raspisanie = KeyboardButton('/Расписание')
news = KeyboardButton('/Новости')
Today = KeyboardButton('/Сегодня')
Tomorrow = KeyboardButton('/Завтра')
After_tomorrow = KeyboardButton('/Послезавтра')
Week = KeyboardButton('/На неделю')
# _______________ _______________#
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
raspis_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


# ____________________Расположение КБ____________________#
raspis_kb.row(Today, Tomorrow, After_tomorrow, Week)
kb_client.row(raspisanie, news)
