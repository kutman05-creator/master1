from  aiogram import  Router , types
from aiogram.filters import  Command
import random

random_router = Router()


NAMES = ['Кутман',"Байэл","Алибек","Баяс","Исмадияр","Актан"]




@random_router.message(Command("random"))
async def random_name(message : types.Message):
    name = random.choice(NAMES)
    await message.answer(f"Случайное имя : {name}")


