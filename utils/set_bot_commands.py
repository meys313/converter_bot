from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("scale_of_notation", "Перевести из одной системы счисления в другую"),
            types.BotCommand("data_converter", "Конвертер единиц измерения информации"),
            types.BotCommand("detect_years", "Определить возраст"),
            types.BotCommand("difference_between_dates", "Определить разницу между двумя датами"),
            types.BotCommand("discount", "Рассчитать скидку"),
            types.BotCommand("default_calculator", "Обычный калькулятор"),
            types.BotCommand("inline_calculator", "Инлайн калькулятор"),
            types.BotCommand("/cancel", "Отмена"),
            types.BotCommand("/help", "Справка"),
        ]
    )
