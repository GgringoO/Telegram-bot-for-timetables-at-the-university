import sqlite3
import sqlite3 as sq
import pandas as pd
from create_bot import bot
import aiosqlite
import datetime


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ Создание базы ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #
def sql_start():
    global base, cur
    base = sq.connect('base_GUMRF.db')
    cur = base.cursor()
    if base:
        print("База подключена!")
    base.execute("""
        CREATE TABLE IF NOT EXISTS Raspisanie (
            time TEXT,
            item TEXT,
            teacher TEXT,
            day TEXT,
            grop INTEGER,
            auditori INTEGER,
            vid TEXT,
            naprav TEXT
            ) """)
    base.execute("""
        CREATE TABLE IF NOT EXISTS News (info TEXT, description TEXT)""")
    base.execute("""
        CREATE TABLE IF NOT EXISTS Users (tg_id INTEGER, name_group TEXT)""")
    base.commit()


# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ Создание базы ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #


async def add_user(user_id):
    cur.execute('INSERT INTO Users VALUES (?, ?)', (user_id, 'no_group'))
    base.commit()


async def add_group(state):
    async with state.proxy() as group:
        grupp = group['grupp']
    cur.execute('UPDATE Users SET name_group = ?', (grupp,))
    base.commit()


async def get_all_users():
    return [u for u in cur.execute('SELECT * FROM Users')]


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ Поиск данных из базы по введенным аргументам ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #


async def sql_sear(message):
    async with aiosqlite.connect('base_GUMRF.db') as base:
        async with base.execute('SELECT name_group FROM Users WHERE tg_id = ?', (message.from_user.id,)) as cur:
            result = await cur.fetchone()
            if result is not None:
                today = datetime.datetime.today().weekday()
                days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
                sed = days[today]
                async with base.execute('SELECT * FROM Raspisanie WHERE naprav = ? and day = ?', (result[0], sed)) as cur:
                    results = await cur.fetchall()
                    for ret in results:
                        await bot.send_message(message.from_user.id, f'''
                        <pre style="font-family: monospace; font-size: 12px">
Время: {ret[0]}\n
Предмет: {ret[1]}\n
Вид: {ret[6]}\n
Преподаватель: {ret[2]}\n
Аудитория: {ret[5]}\n
Группа: {ret[4]}
                        </pre>
                        ''', parse_mode='HTML')
            else:
                await bot.send_message(message.from_user.id, "Группа не найдена")


async def sql_sear2(message):
    async with aiosqlite.connect('base_GUMRF.db') as base:
        async with base.execute('SELECT name_group FROM Users WHERE tg_id = ?', (message.from_user.id,)) as cur:
            result = await cur.fetchone()
            if result is not None:
                today = datetime.datetime.today().weekday()
                days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
                tomorrow = (today + 1) % 7
                sed = days[tomorrow]
                async with base.execute('SELECT * FROM Raspisanie WHERE naprav = ? and day = ?', (result[0], sed)) as cur:
                    results = await cur.fetchall()
                    for ret in results:
                        await bot.send_message(message.from_user.id, f'''
                        <pre style="font-family: monospace; font-size: 12px">
Время: {ret[0]}\n
Предмет: {ret[1]}\n
Вид: {ret[6]}\n
Преподаватель: {ret[2]}\n
Аудитория: {ret[5]}\n
Группа: {ret[4]}
                                                </pre>
                                                ''', parse_mode='HTML')
            else:
                await bot.send_message(message.from_user.id, "Группа не найдена")


async def sql_sear3(message):
    async with aiosqlite.connect('base_GUMRF.db') as base:
        async with base.execute('SELECT name_group FROM Users WHERE tg_id = ?', (message.from_user.id,)) as cur:
            result = await cur.fetchone()
            if result is not None:
                today = datetime.datetime.today().weekday()
                days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
                tomorrow = (today + 2) % 7
                sed = days[tomorrow]
                async with base.execute('SELECT * FROM Raspisanie WHERE naprav = ? and day = ?', (result[0], sed)) as cur:
                    results = await cur.fetchall()
                    for ret in results:
                        await bot.send_message(message.from_user.id, f'''
                        <pre style="font-family: monospace; font-size: 12px">
Время: {ret[0]}\n
Предмет: {ret[1]}\n
Вид: {ret[6]}\n
Преподаватель: {ret[2]}\n
Аудитория: {ret[5]}\n
Группа: {ret[4]}
                        </pre>
                        ''', parse_mode='HTML')
            else:
                await bot.send_message(message.from_user.id, "Группа не найдена")

async def sql_sear4(message):
    async with aiosqlite.connect('base_GUMRF.db') as base:
        async with base.execute('SELECT name_group FROM Users WHERE tg_id = ?', (message.from_user.id,)) as cur:
            result = await cur.fetchone()
            if result is not None:
                today = datetime.datetime.today().weekday()
                days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
                tomorrow = (today + 2) % 7
                sed = days[tomorrow]
                async with base.execute('SELECT * FROM Raspisanie WHERE teacher = ? and day = ?',
                                        (result[0], sed)) as cur:
                    results = await cur.fetchall()
                    for ret in results:
                        await bot.send_message(message.from_user.id, f'''
                            <pre style="font-family: monospace; font-size: 12px">
    Время: {ret[0]}\n
    Предмет: {ret[1]}\n
    Вид: {ret[6]}\n
    Преподаватель: {ret[2]}\n
    Аудитория: {ret[5]}\n
    Группа: {ret[4]}
                            </pre>
                            ''', parse_mode='HTML')
            else:
                await bot.send_message(message.from_user.id, "Группа не найдена")

    # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ Поиск данных из базы по введенным аргументам ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ Функция обнавления данных из Exel в базу ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #

async def add_table():
    read_file = pd.read_excel(r'Расписание.xlsx')

    read_file.to_csv(r'Raspisanie.csv', index=None, header=True)

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ Функция обнавления данных из Exel в базу ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ Импорт в базу ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #

    connection = sqlite3.connect('base_GUMRF.db')
    cursor = connection.cursor()

    with open('Raspisanie.csv', 'r', encoding='UTF8') as file:
        records = 0
        for row in file:
            row_values = row.strip().split(",")
            cursor.execute('INSERT INTO Raspisanie VALUES (?, ?, ?, ?, ?, ?, ?, ?)', tuple(row_values))
            connection.commit()
            records += 1
    connection.close()
    print('\n{} В базу добавлено! Значений:', format(records))

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ Импорт в базу ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ Удаление данных из таблицы ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #

async def del_table():
    cur.execute("DELETE FROM Raspisanie")
    base.commit()

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ Удаление данных из таблицы ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ Новости ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #
async def add_news(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO News VALUES (?, ?)', tuple(data.values()))
        base.commit()


async def del_news():
    cur.execute("DELETE FROM News")
    base.commit()


async def news(message):
    for nw in cur.execute(" SELECT * FROM News"):
        await bot.send_message(message.from_user.id, f'''  {nw[0]}\n {nw[1]}''')
# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ Новости ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #
