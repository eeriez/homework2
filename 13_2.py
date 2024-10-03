import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types

api = '7572593136:AAFMk-WUhbLV456ABBy8m6G2gA-srLr3k8A'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот, помогающий твоему здоровью.')


@dp.message_handler(text=['Urban'])
async def test_message(message):
    print('Urban message')


@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
