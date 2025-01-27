from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from data_base import Database
from bot_config import data_base


dishes_admin_router = Router()
dishes_admin_router.message.filter(
    F.from_user.id == 6669757671
)





class Dishes(StatesGroup):
    name = State()
    price = State()
    category= State()
    portion_option= State()

@dishes_admin_router.message(Command("dishes"))
async def new_book(message: types.Message, state: FSMContext):
    await message.answer("Введите название блюдо")
    await state.set_state(Dishes.name)

@dishes_admin_router.message(Dishes.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену блюдо")
    await state.set_state(Dishes.price)

@dishes_admin_router.message(Dishes.price)
async def process_year(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit():
        await message.answer("Вводите только цифры")
        return
    price = int(price)
    if price <= 0:
        await message.answer("Вводите только положительную цену")
        return

    await state.update_data(price=message.text)
    await message.answer("Введите  категорию блюдо")
    await state.set_state(Dishes.category)

@dishes_admin_router.message(Dishes.category)
async def process_author(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer("Введите варианты порций ")
    await state.set_state(Dishes.portion_option)

@dishes_admin_router.message(Dishes.portion_option)
async def process_price(message: types.Message, state: FSMContext):
    await state.update_data(portion_option=message.text)
    await message.answer("Спасибо, блюдо  была сохранена")
    data = await state.get_data()
    print(data)
    data_base.save_dish(data)
    await state.clear()

