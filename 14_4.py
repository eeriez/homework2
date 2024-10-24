from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import get_all_products

products = get_all_products()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# клавиатуры
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
inline_keyboard = InlineKeyboardMarkup()
products_keyboard = InlineKeyboardMarkup()

# кнопки
start_button = KeyboardButton(text='/start')
begin_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
buy_button = KeyboardButton(text='Купить')
calories_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')
p1_button = InlineKeyboardButton(text='Product1', callback_data='product_buying')
p2_button = InlineKeyboardButton(text='Product2', callback_data='product_buying')
p3_button = InlineKeyboardButton(text='Product3', callback_data='product_buying')
p4_button = InlineKeyboardButton(text='Product4', callback_data='product_buying')

# прилепляем кнопки к клавиатурам
start_keyboard.add(start_button)
keyboard.add(begin_button)
keyboard.add(info_button)
keyboard.add(buy_button)
inline_keyboard.add(calories_button)
inline_keyboard.add(formulas_button)
products_keyboard.add(p1_button)
products_keyboard.add(p2_button)
products_keyboard.add(p3_button)
products_keyboard.add(p4_button)


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=inline_keyboard)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст.')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def fsm_height(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['height']) - 5 * int(data['age']) + 5
    await message.answer(f'Необходмиое количество калорий в день для вас: {calories}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in products:
        await message.answer(f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}')
        with open('C:/Users/eerie/OneDrive/Рабочий стол/тирлист/b526b30e06f14993856537c40c915cf0.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=products_keyboard)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.', reply_markup=start_keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
