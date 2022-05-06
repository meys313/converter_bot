from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from filters import IsDigit
from keyboards.inline.temperature import callback
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline import temperature_keyboard
from states import TemperatureStates

@dp.message_handler(Command('temperature'), state = "*")
async def discount(message: types.Message, state: FSMContext):
    await message.answer('выберите величину из которой вы хотите перевести', reply_markup=temperature_keyboard)
    await state.finish()
    await state.set_state(TemperatureStates.convert_from.state)

@dp.callback_query_handler(callback.filter(), state=TemperatureStates.convert_from)
async def get_from(call: CallbackQuery,  callback_data: dict, state: FSMContext):
    await call.message.delete()
    message = await call.message.answer(f"<b>{callback_data.get('name')}</b> ➡ ")
    message_keyboards = await call.message.answer('выберите величину в которую вы хотите перевести', reply_markup=temperature_keyboard)
    await state.update_data(name1=callback_data.get('name'), v1=callback_data.get('value'), message=message, keyboards=message_keyboards)
    await TemperatureStates.next()
@dp.callback_query_handler(callback.filter(), state=TemperatureStates.convert_to)
async def get_to(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(name2=callback_data.get('name'), v2=callback_data.get('value'),)
    async with state.proxy() as data:
        await data['keyboards'].delete()
        await data['message'].edit_text(f"<b>{data['name1']}</b> ➡ <b>{callback_data.get('name')}</b> \n \n"
                                        f"<i>Отправьте значение</i>")
    await TemperatureStates.next()


@dp.message_handler(IsDigit(), state=TemperatureStates.value)
async def get_value(message: types.Message, state: FSMContext):
    def get_temperature(t_from, t_to, value):
        temperature = {
            'C': {'step': 1, 'default': 0},
            'F': {'step': 1.8, 'default': 32},  # default - единица по цельсию
            'K': {'step': 1, 'default': 273.15, },
            'R': {'step': 1.8, 'default': 491.67, },
            'Re': {'step': 0.8, 'default': 0}
        }
        # получаю значение 0 относительно единицы измерения с которой и в которую перевожу
        default = temperature[t_to]['default'] - temperature[t_from]['default'] / (
                temperature[t_from]['step'] / temperature[t_to]['step'])

        return default + temperature[t_to]['step'] / temperature[t_from]['step'] * value


    async with state.proxy() as data:
        result = get_temperature(data['v1'], data['v2'], int(message.text))
        await message.answer(f"<b>{result}</b>")
    await state.finish()

@dp.message_handler(state=TemperatureStates.value)
async def incorrect_data(message: types.Message):
    await message.answer('значение может быть только числом. Попробуйте снова')