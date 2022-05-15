from loader import dp
from .users import *

if __name__ == "filters":
    dp.filters_factory.bind(MyFilter)
    dp.filters_factory.bind(InlineClear)
    dp.filters_factory.bind(InlineDelete)
    dp.filters_factory.bind(IsDigit)
    dp.filters_factory.bind(DiscountFilter)



