from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from create_bot import bot
from keyboards import kb_client, raspis_kb
from data_base import sqlite_db


class StartStates(StatesGroup):
    group_name = State()


async def command_start(message: types.Message):
    all_users_id = [id_[0] for id_ in await sqlite_db.get_all_users()]
    if message.from_user.id not in all_users_id:
        await sqlite_db.add_user(message.from_user.id)
    await bot.send_message(message.from_user.id, text='Здравствуйте, это бот расписание ГУМРФ.')
    await bot.send_message(message.from_user.id, text='Укажите вашу группу (Пример: ИТ-1):')
    await StartStates.group_name.set()


async def add_group(message: types.Message, state=FSMContext):
    if message.text == 'ИТ-1':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'ИТ-2':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'ИТ-3':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'ИТ-4':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Ю-1':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Ю-2':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Ю-3':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Ю-4':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Ю-5':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Э-1':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Э-2':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Э-3':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Э-4':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    elif message.text == 'Э-5':
        async with state.proxy() as group:
            group['grupp'] = message.text
        await sqlite_db.add_group(state)
        await message.reply(f'Вы привязаны к группе: {message.text}', reply_markup=kb_client)
        await state.finish()
    else:
        await message.reply(f'Такой группы нету! Попробуйте заново')
        await state.finish()


# ............................................Pасписание............................................#


async def raspis(message: types.Message):
    await bot.send_message(message.from_user.id, text='Выберите день', reply_markup=raspis_kb)


async def today(message: types.Message):
    await sqlite_db.sql_sear(message)
    await bot.send_message(message.from_user.id, text='Выберите день', reply_markup=raspis_kb)


async def tomorrow(message: types.Message):
    await sqlite_db.sql_sear2(message)
    await bot.send_message(message.from_user.id, text='Выберите день', reply_markup=raspis_kb)


async def after_tomorrow(message: types.Message):
    await sqlite_db.sql_sear3(message)
    await bot.send_message(message.from_user.id, text='Выберите день', reply_markup=raspis_kb)


# ............................................Pасписание............................................#


async def command_news(message: types.Message):
    await sqlite_db.news(message)


# _______ Команда Help _______ #
async def helps(message: types.Message):
    await bot.send_message(message.from_user.id, '''
    Это помощник бота ГУМРФ, здесь прописан весь функционал пользователя:
    /start - Начальная команда для запуска диалога с ботом
    /Расписание - Команда для расписания
    /news - Команда для просмотра новостей вуза
    /help - Команда помощник
    ''')



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(add_group, state=StartStates.group_name)
    dp.register_message_handler(command_news, commands=['news'])
    dp.register_message_handler(helps, commands=['help'])
    dp.register_message_handler(raspis, commands=['Расписание'])
    dp.register_message_handler(today, commands=['Сегодня'])
    dp.register_message_handler(tomorrow, commands=['Завтра'])
    dp.register_message_handler(after_tomorrow, commands=['Послезавтра'])
