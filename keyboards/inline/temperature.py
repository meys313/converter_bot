from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'name', "value")
temperature_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Цельсий °C', callback_data=callback.new(name="°C", value="C"))],
    [InlineKeyboardButton(text='Фаренгейт °F', callback_data=callback.new(name="°F", value="F"))],
    [InlineKeyboardButton(text='Кельвин K', callback_data=callback.new(name="K", value="K"))],
    [InlineKeyboardButton(text='Ранкин °R', callback_data=callback.new(name="°R", value="R"))],
    [InlineKeyboardButton(text='Реомюр °Re', callback_data=callback.new(name="°Re", value="Re"))],
])
