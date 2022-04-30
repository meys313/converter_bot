from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'name', 'value')


data_converter_keyboard = InlineKeyboardMarkup(
                                          inline_keyboard= [
                                              #[InlineKeyboardButton(text='Байт', callback_data=callback.new(name='Байт', value=1))],
                                              [InlineKeyboardButton(text='Килобайт', callback_data=callback.new(name='килобайт', value=1))],
                                              [InlineKeyboardButton(text='Мегабайт', callback_data=callback.new(name='мегабайт', value=2))],
                                              [InlineKeyboardButton(text='Гигабайт', callback_data=callback.new(name='гигабайт', value=3))],
                                              [InlineKeyboardButton(text='Терабайт', callback_data=callback.new(name='терабайт', value=4))],
                                              [InlineKeyboardButton(text='Петабайт', callback_data=callback.new(name='петабайт', value=5))],


                                          ])
