from  aiogram import  Router , types
from aiogram.filters import  Command

myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def my_info(message: types.Message):
    name = message.from_user.first_name
    name2 = message.from_user.username
    idd = message.from_user.id
    await message.answer(f"Имя: {name}\n"
                         f"Пользователь: {name2}\n "
                         f"Айди: {idd}\n")