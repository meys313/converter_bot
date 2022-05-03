from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'name', 'value')
scale_of_notation_keyboard = InlineKeyboardMarkup(
                                          inline_keyboard= [
                                              [InlineKeyboardButton(text='Определить автоматичски', callback_data=callback.new(name='AUTO', value=0))],
                                              [InlineKeyboardButton(text='Двоичная BIN', callback_data=callback.new(name='BIN', value=2))],
                                              [InlineKeyboardButton(text='Восьмеричная OCT', callback_data=callback.new(name="OCT", value=8))],
                                              [InlineKeyboardButton(text='Десятичная DEC', callback_data=callback.new(name='DEC', value=10))],
                                              [InlineKeyboardButton(text='Шестнадцатеричная HEX', callback_data=callback.new(name="HEX", value=16))],
                                          ])

