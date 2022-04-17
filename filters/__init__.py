from loader import dp
from .users import MyFilter

if __name__ == "filters":
    dp.filters_factory.bind(MyFilter)