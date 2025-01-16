from  aiogram import types , Router

other_router = Router()

@other_router.message()
async def echo_handler(message: types.Message):
    await message.answer("Я вас не понимаю")