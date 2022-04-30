from aiogram.dispatcher.filters.state import State, StatesGroup


year = State("year")


class DiscountState(StatesGroup):
    price = State()
    discount = State()


class States_difference_date(StatesGroup):
    data_1 = State()
    data_2 = State()

class DataConverterState(StatesGroup):
    convert_from = State()
    convert_to = State()
    value = State()
