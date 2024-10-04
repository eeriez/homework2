from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
inline_keyboard = InlineKeyboardMarkup()

start_button = KeyboardButton(text='/start')
begin_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
calories_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')

start_keyboard.add(start_button)
keyboard.add(begin_button)
keyboard.add(info_button)
inline_keyboard.add(calories_button)
inline_keyboard.add(formulas_button)


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


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.', reply_markup=start_keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
