import re
from aiogram import types


from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery


class MyFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        character_dict = {'➕': '+', '➖': '-', '✖': '*', '➗': '/'}
        if message.text in character_dict:
            message.text = character_dict[message.text]
            return message.text
        else:
            if re.findall(r"^[0-9 .+*\/-]*$", message.text):
                return True

class InlineClear(BoundFilter):
    async def check(self, call: CallbackQuery) -> bool:
        return call.data.split(":")[-1] == "clear"


class InlineDelete(BoundFilter):
    async def check(self, call: CallbackQuery) -> bool:
        return call.data.split(":")[-1] == "delete"

