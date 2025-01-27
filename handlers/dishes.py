from aiogram import Router,F,types
from pprint import pprint


from bot_config import data_base

catalog_router = Router()

@catalog_router.callback_query(F.data == "dishes")
async def catalog_handler(callback:types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наш каталог блюд")
    dish_list = data_base.get_all_dishes()
    pprint(dish_list)
    for dish in dish_list:
        await callback.message.answer(f"Название бдюдо :{dish.get('name','Без названия')}\n Цена блюдо:{dish.get('price')}\nКатегория блюдо:{dish.get('category')}\nПорция блюдо:{dish.get('portion_option')}")

