from  aiogram import  Router,types,F
from  aiogram.fsm.context import FSMContext
from  aiogram.fsm.state import State , StatesGroup

review_router = Router()

class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()

@review_router. callback_query(F.data == "review")
async def  process_name(call: types.CallbackQuery,state: FSMContext) :
    await call.message.answer ("Как Baс зовут?")
    await state.set_state (RestaurantReview.name )



@review_router.message(RestaurantReview.name)
async def process_phone_number(message: types.Message, state: FSMContext):
    await message. answer ("Ваш номер телефона")
    await state.set_state(RestaurantReview.phone_number)


@review_router.message(RestaurantReview.phone_number)
async def process_review (message: types.Message, state: FSMContext) :
    await message. answer ("Поставьте нам оценку от 1 до 5")
    await state.set_state(RestaurantReview.rate)


@review_router.message(RestaurantReview.rate)
async def extra_process(message: types.Message, state: FSMContext):
    await message.answer("Дополнительные комментарии/жалоба")
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments)
async def finish_process(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ваш отзыв")
    await state.set_state(RestaurantReview.extra_comments)
    await state.clear()

