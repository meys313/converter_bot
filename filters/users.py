import re
from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import BoundFilter, state
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


# проверяет, является ли принятое сообщение исключительно числом
class IsDigit(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.text.isdigit()


class DiscountFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return 0 < int(message.text) <= 100
