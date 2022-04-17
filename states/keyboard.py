from aiogram.dispatcher.filters.state import State, StatesGroup

class StatesKeyboard(StatesGroup):
    number = State()
    message_id = State()


