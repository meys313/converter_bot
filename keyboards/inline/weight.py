from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'name', "value")
weight_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Тонна', callback_data=callback.new(name="T", value=5))],
    [InlineKeyboardButton(text='Киллограмм', callback_data=callback.new(name="КГ", value=4))],
    [InlineKeyboardButton(text='Грамм', callback_data=callback.new(name="Г", value=3))],
    [InlineKeyboardButton(text='Миллиграмм', callback_data=callback.new(name="МГ", value=2))],
    [InlineKeyboardButton(text='Микрограмм', callback_data=callback.new(name="мкг", value=1))],

])
