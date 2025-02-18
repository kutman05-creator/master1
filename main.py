import  asyncio
import logging


from handlers.group import ban_router
from bot_config import  dp, bot , data_base
from  aiogram import Bot
# from handlers.dishes_mang import dishes_admin_router
from  handlers.start import  start_router
from  handlers.myinfo import  myinfo_router
from  handlers.random import  random_router
from  handlers.picture import  picture_router
from  handlers.review_dialog import review_router
from  handlers.other_router import other_router
from  handlers.dishes_mang import dishes_admin_router
from  handlers.dishes import catalog_router

async def on_startup(bot: Bot):
    data_base.create_table()






async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_router)
    dp.include_router(picture_router)
    dp.include_router(review_router)
    dp.include_router(dishes_admin_router)
    dp.include_router(catalog_router)
    dp.include_router(ban_router)
    dp.include_router(other_router)
    # dp.startup.register(on_startup)
    dp.startup.register(on_startup)

    await  dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

