from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = '7572593136:AAEdAWtyD8THstjQq_xH8UX_zHSSHpaSbvA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

start_button = KeyboardButton(text='/start')
begin_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')

start_keyboard.add(start_button)
keyboard.add(begin_button)
keyboard.add(info_button)


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()


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
  
