from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from data_base import Database

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
data_base = Database("dp.sqlite3")
