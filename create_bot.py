from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token='Your token')
dp = Dispatcher(bot, storage=MemoryStorage())
