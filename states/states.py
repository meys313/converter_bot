from aiogram.dispatcher.filters.state import State, StatesGroup


year = State("year")


class States_difference_date(StatesGroup):
    data_1 = State()
    data_2 = State()