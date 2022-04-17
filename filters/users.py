import re
from aiogram import types


from aiogram.dispatcher.filters import BoundFilter


class MyFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        character_dict = {'➕': '+', '➖': '-', '✖': '*', '➗': '/'}
        if message.text in character_dict:
            message.text = character_dict[message.text]
            return message.text
        else:
            if re.findall(r"^[0-9 .+*\/-]*$", message.text):
                return True
