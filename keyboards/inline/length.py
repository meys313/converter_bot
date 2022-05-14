from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'name', "value")
length_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Миллиметры', callback_data=callback.new(name="ММ", value=2))],
    [InlineKeyboardButton(text='Сантиметры', callback_data=callback.new(name="СМ", value=3))],
    [InlineKeyboardButton(text='Метры', callback_data=callback.new(name="М", value=5))],
    [InlineKeyboardButton(text='Километры', callback_data=callback.new(name="КМ", value=8))],
])
