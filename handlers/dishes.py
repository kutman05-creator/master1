from aiogram import Router,F,types
from pprint import pprint
from aiogram_widgets.pagination import TextPaginator


from bot_config import data_base

catalog_router = Router()

@catalog_router.callback_query(F.data == "dishes")
async def catalog_handler(callback:types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наш каталог блюд")
    dish_list = data_base.get_all_dishes()
    pprint(dish_list)
    for dish in dish_list:
        cover = dish.get('cover')
        await callback.message.answer_photo(
            photo = cover,
            caption = f"Название бдюдо : {dish.get('name','Без названия')}\n "
                      f"Цена блюдо: {dish.get('price')}\n"
                      f"Категория блюдо: {dish.get('category')}\n"
                      f"Порция блюдо: {dish.get('portion_option')}"
        )

@catalog_router.callback_query(F.data =='dish_catalog_pagination')
async def catalog_pagination_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наш каталог блюд")
    dish_list = data_base.get_all_dishes()
    pprint(dish_list)

    text_data = [
        f"Название бдюдо : {dish.get('name', 'Без названия')}\n "
        f"Цена блюдо: {dish.get('price')}\n"
        f"Категория блюдо: {dish.get('category')}\n"
        f"Порция блюдо: {dish.get('portion_option')}\n" 
        f"Фото вашего блюдо: {dish.get('cover')}" for dish in dish_list

    ]
    paginator = TextPaginator(data = text_data,router = catalog_router,per_page = 1)
    current_text_chunk, reply_markup = paginator.current_message_data
    await callback.message.answer(
        text=current_text_chunk,
        reply_markup=reply_markup
    )