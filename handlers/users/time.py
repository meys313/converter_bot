from aiogram import types

from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from filters import IsDigit
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline import time_keyboard
from keyboards.inline.time import callback
from states import TimeStates



@dp.message_handler(Command('time'), state="*")
async def get_command(message: types.Message, state: FSMContext):
    await state.finish()
    await state.set_state(TimeStates.data_from)
    await message.answer('выберите величину из которой вы хотите перевести',
                         reply_markup=time_keyboard)

@dp.callback_query_handler(callback.filter(), state=TimeStates.data_from)
async def get_from(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    message = await call.message.answer(f"<b>{callback_data.get('name')}</b> ➡ ")

    message_keyboards = await call.message.answer('Выберите величину в которую вы хотите перевести',
                                                  reply_markup=time_keyboard)
    await state.update_data(name1=callback_data.get('name'), message=message,
                            keyboards=message_keyboards)
    await TimeStates.next()


@dp.callback_query_handler(callback.filter(), state= TimeStates.data_to)
async def get_to(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(name2=callback_data.get('name'))
    async with state.proxy() as data:
        await data['keyboards'].delete()
        await data['message'].edit_text(f"<b>{data['name1']}</b> ➡ <b>{callback_data.get('name')}</b> \n \n"
                                        f"<i>Отправьте значение</i>")
    await TimeStates.next()

@dp.message_handler(IsDigit(), state=TimeStates.value)
async def get_value(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        def get_time(type, value):
            from_type_to_seconds = {
                'minutes': value * 60,
                'hours': (value * 60) * 60,
                'days': (value * 24) * 3600,
                'weeks': 3600 * ((value * 7) * 24)
            }
            get_seconds = from_type_to_seconds[type]
            seconds = get_seconds
            minutes = get_seconds / 60
            hours = minutes / 60
            days = hours / 24
            weeks = days / 7

            return {'seconds': seconds, 'minutes': minutes, 'hours': hours, 'days': days, 'weeks': weeks}

        value = int(message.text)
        result = get_time(data['name1'], value)[data['name2']]

        await message.answer(f"{value} {data['name1']} ➡ {data['name2']}: \n"
                             f"<b>{result}</b> {data['name2']}")


@dp.message_handler(state=TimeStates.value)
async def incorrect_data(message: types.Message, state: FSMContext):
    await message.answer('значение может быть только числом. Попробуйте снова')