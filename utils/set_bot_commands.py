from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("/cancel", "Отмена действия / Выход из команды"),
            types.BotCommand("/command", "Список команд"),
            types.BotCommand("currency", "конвертер валют"),
            types.BotCommand("temperature", "конвертер единиц измерения температуры"),
            types.BotCommand("length", "конвертер единиц измерения длины"),
            types.BotCommand("weight", "конвертер единиц измерения массы"),
            types.BotCommand("time", "конвертер времени"),
            types.BotCommand("scale_of_notation", "Перевести из одной системы счисления в другую"),
            types.BotCommand("detect_years", "Определить возраст"),
            types.BotCommand("data_converter", "конвертер единиц измерения кол-ва информации"),
            types.BotCommand("difference_between_dates", "Определить разницу между двумя датами"),
            types.BotCommand("discount", "Рассчитать скидку"),
            types.BotCommand("default_calculator", "Обычный калькулятор"),
            types.BotCommand("inline_calculator", "Инлайн калькулятор"),
        ]
    )
