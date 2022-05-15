from aiogram import types
from loader import dp
from states import cancel


@dp.message_handler()
async def all_text(message: types.Message):
    await message.reply('Команда не распознана, список всех комманд - /command')


@dp.message_handler(state=cancel)
async def all_text(message: types.Message):
    await message.reply('Команда не распознана, список всех комманд - /command')
