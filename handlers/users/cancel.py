from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import StateFilter
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from states import cancel


@dp.message_handler(Command('cancel'), state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(cancel)


@dp.message_handler(filters.Regexp(r"^[/][a-zA-Z_]+$"), ~StateFilter(dp, state=None), ~StateFilter(dp, state=cancel),
                    state='*')
async def not_set_cancel(message: types.Message, state: FSMContext):
    await message.answer('Похоже, что вы пытаетесь отправить боту команду, работая с другой командой. Выйти - /cancel')
