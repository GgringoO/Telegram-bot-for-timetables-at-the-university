from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from data_base import sqlite_db
import datetime
import os


ID = None


class FsmAdmin(StatesGroup):
    info = State()
    description = State()


async def admin_dostup(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, '''Здравствуйте, администратор, что будем делать? 
    Для информации пропишите "/helpAdmin"''')
    await message.delete()


async def exit_admin(message: types.Message):
    global ID
    if message.from_user.id == ID:
        ID = None
        await bot.send_message(message.from_user.id, 'Вы успешно вышли из административного режима')
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором')
    await message.delete()


# ____________________Добавление новости____________________ #

async def add_news(message: types.Message):
    if message.from_user.id == ID:
        await message.reply("Добавьте заголовок новости:")
        await FsmAdmin.info.set()
    else:
        await message.reply('Вы не являетесь администратором!')


async def load_info(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['info'] = message.text
        await message.reply("Введите содержание новости:")
        await FsmAdmin.next()
    else:
        await message.reply('Вы не являетесь администратором!')


async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await sqlite_db.add_news(state)
        await message.reply("Новость добавлена")
        await state.finish()
    else:
        await message.reply('Вы не являетесь администратором!')


# _______________Отмена добавления_______________ #
async def news_cancel(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        cur_st = await state.get_state()
        if cur_st is None:
            return
        await message.reply('Добавление новости отменено!')
        await state.finish()
    else:
        await message.reply('Вы не являетесь администратором!')


async def del_news(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.del_news()
        await message.reply('Новости удалены')
    else:
        await message.reply('Вы не являетесь администратором!')
# ____________________Добавление новости____________________#


# ____________________Добавление данных из Exel____________________#

async def add_sql(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.add_table()
        await message.reply('Данные базы обновлены!')
    else:
        await message.reply('Вы не являетесь администратором!')
# ____________________Добавление данных из Exel____________________#


# ____________________Удаление данных из базы____________________#

async def del_sql(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.del_table()
        await message.reply('Данные базы удалены!')
    else:
        await message.reply('Вы не являетесь администратором!')


# ____________________Удаление данных из базы____________________#


async def helps(message: types.Message):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id, '''
        Это помощник бота ГУМРФ, здесь прописан весь функционал администратора:\n
        /Admin - Команда админ служит служебной командой для 
        администраторов бота,
        при запуске команды доступны все команды 
        администратора (прописанные ниже)\n 
        /NoAdmin - Команда для выхода из режима администратора\n 
        /Restart - перезагрузка бота\n
        /Add_News - Команда администратора для добавления 
        новостей,
        при отмене добавления новости пропишите команду 
        "/Отмена".\n 
        /Del_News - Удаление новостей\n
        /AddSQL - Команда администратора для добавления в 
        базу данных о расписании их exel.
        (Внимание! При использовании команды, убедитесь, что
        база данных очищена от старых данных!)\n 
        /DelSQL - Команда администратора для удаления данных из
        базы.
        (Внимание! После удаления данных перезапустите бота)\n 
        ''')
    else:
        await message.reply('Вы не являетесь администратором!')


async def restart_bot(message: types.Message):
    if message.from_user.id == ID:
        restart_time = datetime.datetime.now()
        await message.answer(f"Бот перезагружается. Время перезагрузки: {restart_time}")
        os.system("python bot_GUMRF.py")
    else:
        await message.reply('Вы не являетесь администратором!')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_dostup, commands=['Admin'], is_chat_admin=True)
    dp.register_message_handler(exit_admin, commands=['NoAdmin'], is_chat_admin=True)
    dp.register_message_handler(restart_bot, commands=['Restart'])
    dp.register_message_handler(add_news, commands=['Add_News'])
    dp.register_message_handler(del_news, commands=['Del_News'])
    dp.register_message_handler(helps, commands=['helpAdmin'])
    dp.register_message_handler(load_info, state=FsmAdmin.info)
    dp.register_message_handler(load_description, state=FsmAdmin.description)
    dp.register_message_handler(news_cancel, state="*", commands='Отмена')
    dp.register_message_handler(news_cancel, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(add_sql, commands=['AddSQL'], state=None)
    dp.register_message_handler(del_sql, commands=['DelSQL'], state=None)
