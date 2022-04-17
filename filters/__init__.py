from loader import dp
from .users import MyFilter, InlineClear, InlineDelete

if __name__ == "filters":
    dp.filters_factory.bind(MyFilter)
    dp.filters_factory.bind(InlineClear)
    dp.filters_factory.bind(InlineDelete)
