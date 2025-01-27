from  aiogram import  Router , types,F,Dispatcher
from aiogram.filters import  Command
start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    # message.from_user.id
    # await message.answer(f"Привет, {name}")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com")
            ],
            [
                types.InlineKeyboardButton(
                    text="Оставить отзыв", callback_data="review"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Все блюдо", callback_data="dishes"
                )

            ]

        ]
    )
    await message.answer(f"Привет, {name}", reply_markup=kb)





