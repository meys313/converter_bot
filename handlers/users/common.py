from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import Command
from loader import dp, bot
from aiogram.dispatcher import FSMContext




@dp.message_handler(Command('cancel'), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())