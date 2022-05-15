from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'name')
all_currency_callback = CallbackData('all_currency')
currency_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text='Рубль', callback_data=callback.new(name="ММ"))],
    # [InlineKeyboardButton(text='Ввести валюту заново', callback_data=callback.new(name="ММ"))],
    # [InlineKeyboardButton(text='Все валюты (большой список)', callback_data=callback.new())],
])
