from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from keyboards.inline.scale_of_notation import callback
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline import scale_of_notation_keyboard
from states import ScaleOfNotationState


@dp.message_handler(Command('scale_of_notation'), state="*")
async def get_command(message: types.Message, state: FSMContext):
    await state.finish()
    await state.set_state(ScaleOfNotationState.convert_from)
    keyboards = scale_of_notation_keyboard
    await message.answer('выберите систему счисления из которой вы хотите перевести',
                         reply_markup=keyboards)
    await state.update_data(keyboards=keyboards)


@dp.callback_query_handler(callback.filter(), state=ScaleOfNotationState.convert_from)
async def get_from(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    message = await call.message.answer(f"<b>{callback_data.get('name')}</b> ➡ ")
    keyboards = (await state.get_data())['keyboards']
    keyboards.inline_keyboard.pop(0)  # Удаляю кнопку с возможностью выбрать систему счисления автомат.
    message_keyboards = await call.message.answer('выберите систему счисления в которую вы хотите перевести',
                                                  reply_markup=keyboards)
    await state.update_data(name1=callback_data.get('name'), v1=callback_data.get('value'), message=message,
                            keyboards=message_keyboards)
    await ScaleOfNotationState.next()


@dp.callback_query_handler(callback.filter(), state=ScaleOfNotationState.convert_to)
async def get_to(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(name2=callback_data.get('name'), func=callback_data.get('func'))
    async with state.proxy() as data:
        await data['keyboards'].delete()
        await data['message'].edit_text(f"<b>{data['name1']}</b> ➡ <b>{callback_data.get('name')}</b> \n \n"
                                        f"<i>Отправьте значение</i>")
    await ScaleOfNotationState.next()


@dp.message_handler(state=ScaleOfNotationState.value)
async def get_value(message: types.Message, state: FSMContext):
    scales_of_notation = {
        'BIN': bin,
        'OCT': oct,
        'DEC': int,
        'HEX': hex
    }
    async with state.proxy() as data:
        try:
            if data['v1'] != '0':
                get_dec = int(message.text, int(data['v1']))
            else:
                get_dec = int(message.text, 0)

        except ValueError:
            return await message.answer('Введены некорректные данные')

        result = scales_of_notation[data['name2']](get_dec)
        result_slice = result
        if type(result) == str:
            result_slice = result[2:]

    await state.finish()
    return await message.answer(f"<b>{result_slice} \n"
                                f"[ <code>{result}</code> ]</b>")
