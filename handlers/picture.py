from  aiogram import  Router , types
from aiogram.filters import  Command


picture_router = Router()


@picture_router.message(Command("picture"))
async def send_picture_handler(message: types.Message):
    one_photo = types.FSInputFile("Imagges/one_peace.jpg")
    await message.answer_photo(
        photo = one_photo,
        caption="Я стану королем Пиратов"



    )
