from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

calculator = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='7'),
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
            KeyboardButton(text='✖'),
        ],

        [
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
            KeyboardButton(text='➗'),
        ],

        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
            KeyboardButton(text='➖'),
        ],

        [
            KeyboardButton(text='0'),
            KeyboardButton(text='.'),
            KeyboardButton(text='='),
            KeyboardButton(text='➕'),
        ],

    ]


)