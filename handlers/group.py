
from aiogram import Router, types, F


ban_router = Router()

# ban_router.message.filter(F.chat.type != 'private')


ban_router.message.filter(F.chat.type.in_({"group", "supergroup"}))


BAD_WORDS = ["дурак", "тупой", "изгой", "блин", "дубина"]

@ban_router.message(F.text)
async def check_bad_words(message: types.Message):
    if message.text:
        words = message.text.lower().split()

        for bad_word in BAD_WORDS:
            if bad_word in words:

                await message.answer(
                    f"{message.from_user.full_name}, вы нарушили правила и будете забанены!",
                    reply_to_message_id=message.message_id
                )
                await message.chat.ban(message.from_user.id)
                break

















