from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callbackButton = CallbackData('callbackButton', 'value')

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="CLEAR", callback_data= callbackButton.new(value='clear'))],
])