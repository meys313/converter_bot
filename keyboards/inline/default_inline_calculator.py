from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('callback', 'value')


default_calculator = InlineKeyboardMarkup(row_width=5,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='1', callback_data=callback.new(value='1')),
                                                  InlineKeyboardButton(text='2', callback_data=callback.new(value='2')),
                                                  InlineKeyboardButton(text='3', callback_data=callback.new(value='3')),
                                                  InlineKeyboardButton(text='4', callback_data=callback.new(value='4')),
                                                  InlineKeyboardButton(text='5', callback_data=callback.new(value='5')),
                                              ],
                                              [
                                                  InlineKeyboardButton(text='6', callback_data=callback.new(value='6')),
                                                  InlineKeyboardButton(text='7', callback_data=callback.new(value='7')),
                                                  InlineKeyboardButton(text='8', callback_data=callback.new(value='8')),
                                                  InlineKeyboardButton(text='9', callback_data=callback.new(value='9')),
                                                  InlineKeyboardButton(text='0', callback_data=callback.new(value='0')),
                                              ],

                                              [
                                                  InlineKeyboardButton(text='+', callback_data=callback.new(value='+')),
                                                  InlineKeyboardButton(text='-', callback_data=callback.new(value='-')),
                                                  InlineKeyboardButton(text='÷', callback_data=callback.new(value='/')),
                                                  InlineKeyboardButton(text='*', callback_data=callback.new(value='*')),
                                              ],
                                              [
                                                  InlineKeyboardButton(text='=', callback_data=callback.new(value='='))
                                              ]
                                          ])




