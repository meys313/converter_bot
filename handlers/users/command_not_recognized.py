from aiogram import types
from loader import dp

@dp.message_handler()
async def all_text(message: types.Message):
    await message.reply('Команда не распознана, обратитесь к /help')