from aiogram.utils.callback_data import CallbackData
from bs4 import BeautifulSoup
import requests

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery, InlineKeyboardButton

from filters import IsDigit

from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline import currency_keyboard

from states import CurrencyStates
from datetime import date
callback = CallbackData('callback', "name")


def get_currency():
    xml_document = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").content
    soup = BeautifulSoup(xml_document, features="xml")
    currency = {}
    for element in soup.find('ValCurs'):
        char_code = element.find('CharCode').text
        nominal = element.find('Nominal').text
        name = element.find('Name').text
        value = element.find('Value').text
        currency_keyboard.inline_keyboard.append(
            [InlineKeyboardButton(text=name, callback_data=callback.new(char_code))],) # Создаю кнопки в клавиатуре
        # Словарь вида 'USD': {'full_name': 'Доллар США', 'nominal': '1', 'value': '67,3843'},
        currency.update({char_code: {'full_name': name, 'nominal': nominal, 'value': value}})

    return currency


@dp.message_handler(Command('currency'), state="*")
async def discount(message: types.Message, state: FSMContext):
    currency = get_currency()
    await message.answer('выберите валюту из которой хотите конвертировать', reply_markup=currency_keyboard)
    await state.finish()
    await state.set_state(CurrencyStates.convert_from.state)
    await state.update_data(currency=currency)

@dp.callback_query_handler(callback.filter(), state=CurrencyStates.convert_from)
async def get_from(call: CallbackQuery,  callback_data: dict, state: FSMContext):
    await call.message.delete()
    message = await call.message.answer(f"<b>{callback_data.get('name')}</b> ➡ ")
    message_keyboards = await call.message.answer('выберите величину в которую вы хотите перевести', reply_markup=currency_keyboard)
    await state.update_data(name1=callback_data.get('name'), message=message, keyboards=message_keyboards)
    await CurrencyStates.next()
@dp.callback_query_handler(callback.filter(), state=CurrencyStates.convert_to)
async def get_to(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(name2=callback_data.get('name'))
    async with state.proxy() as data:
        await data['keyboards'].delete()
        await data['message'].edit_text(f"<b>{data['name1']}</b> ➡ <b>{callback_data.get('name')}</b> \n\n"
                                        f"<i>Отправьте значение</i>")
    await CurrencyStates.next()


@dp.message_handler(IsDigit(), state=CurrencyStates.value)
async def get_value(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        currency_from = float(data['currency'][data['name1']]['value'].replace(',', '.'))
        nominal_from = float(data['currency'][data['name1']]['nominal'])

        currency_to = float(data['currency'][data['name2']]['value'].replace(',', '.'))
        nominal_to = float(data['currency'][data['name2']]['nominal'])

        convert = round((currency_from / nominal_from) / (currency_to / nominal_to) * int(message.text), 2)

        await message.answer(f"<b>{convert}</b> \n\n"
                             f"Курсы к рублю:\n\n"
        f"Курс {data['name1']}: <b>{currency_from}</b>, номинал: {nominal_from} \n"
                             f" курс {data['name2']}: <b>{currency_to}</b>, номинал: {nominal_to} \n"
        f"<i>Курсы валют предоставлены центральным банком России на момент "
                             f"{message.date.date()}</i>")



@dp.message_handler(state=CurrencyStates.value)
async def incorrect_data(message: types.Message):
    await message.answer('значение может быть только числом. Попробуйте снова')
