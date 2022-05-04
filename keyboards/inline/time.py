from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'name', )
time_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Секунды', callback_data=callback.new(name="seconds"))],
    [InlineKeyboardButton(text='Минуты', callback_data=callback.new(name="minutes"))],
    [InlineKeyboardButton(text='Часы', callback_data=callback.new(name="hours"))],
    [InlineKeyboardButton(text='Дни', callback_data=callback.new(name="days"))],
    [InlineKeyboardButton(text='Недели', callback_data=callback.new(name="weeks"))],

])
