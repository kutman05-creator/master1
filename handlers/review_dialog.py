from  aiogram import  Router,types,F
from  aiogram.fsm.context import FSMContext
from  aiogram.fsm.state import State , StatesGroup
# from  data_base import  Database
from bot_config import data_base

review_router = Router()

class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()
    day_data = State()

@review_router. callback_query(F.data == "review")
async def  process_name(call: types.CallbackQuery,state: FSMContext) :
    await call.message.answer ("Как Baс зовут?")
    await state.set_state (RestaurantReview.name )



@review_router.message(RestaurantReview.name)
async def process_phone_number(message: types.Message, state: FSMContext):
    name = message.text
    await  state.update_data(name = name)
    await message. answer ("Ваш номер телефона")
    await state.set_state(RestaurantReview.phone_number)



@review_router.message(RestaurantReview.phone_number)
async def process_review (message: types.Message, state: FSMContext) :
    phone_number = message.text
    await  state.update_data(phone_number = phone_number)
    await message. answer ("Поставьте нам оценку от 1 до 5")
    await state.set_state(RestaurantReview.rate)


@review_router.message(RestaurantReview.rate)
async def extra_process(message: types.Message, state: FSMContext):
    rate = message.text
    await  state.update_data(rate=rate)
    await message.answer("Дата вашего посещения")
    await state.set_state(RestaurantReview.day_data)


@review_router.message(RestaurantReview.day_data)
async def visit_data(message: types.Message, state: FSMContext):
    data = message.text
    await  state.update_data(data = data)
    await message.answer("Дополнительные комментарии/жалоба")
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments)
async def finish_process(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await  state.update_data(extra_comments = extra_comments)
    await message.answer("Спасибо за ваш отзыв")
    dt = await state.get_data()
    # await state.set_state(RestaurantReview.extra_comments)
    print(dt)
    data_base.save_review(dt)
    await state.clear()

