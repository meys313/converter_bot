from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/cancel - Отменить действие ",
            "/default_calculator - обычный калькулятор",
            "/inline_calculator - инлайн калькутяор",
            "/help - Справка",
            "/discount - Рассчитать скидку",
            "/difference_between_dates - Определить разницу между двумя датами",
            "/detect_years - Определить возраст",
            "/detect_years - Определить возраст и через сколько следующий день рождения",
            "/scale_of_notation - Перевести из одной системы счисления в другую",
            "/time - конвертер времени",
            "/weight - конвертер единиц измерения массы",
            "/length - конвертер единиц измерения длины",
            "/temperature - конвертер единиц измерения температуры",
            "/currency - конвертер валют"
            )
    
    await message.answer("\n".join(text))
