from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

count = CallbackData('count', 'number')
operator = CallbackData('operator', 'operator')

default_calculator = InlineKeyboardMarkup(row_width=5,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='1', callback_data=count.new(number='1')),
                                                  InlineKeyboardButton(text='2', callback_data=count.new(number='2')),
                                                  InlineKeyboardButton(text='3', callback_data=count.new(number='3')),
                                                  InlineKeyboardButton(text='4', callback_data=count.new(number='4')),
                                                  InlineKeyboardButton(text='5', callback_data=count.new(number='5')),
                                              ],
                                              [
                                                  InlineKeyboardButton(text='6', callback_data=count.new(number='6')),
                                                  InlineKeyboardButton(text='7', callback_data=count.new(number='7')),
                                                  InlineKeyboardButton(text='8', callback_data=count.new(number='8')),
                                                  InlineKeyboardButton(text='9', callback_data=count.new(number='9')),
                                                  InlineKeyboardButton(text='0', callback_data=count.new(number='0')),
                                              ],

                                              [
                                                  InlineKeyboardButton(text='+', callback_data=operator.new(operator='+')),
                                              ]
                                          ])




