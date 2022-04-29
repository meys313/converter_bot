from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("detect_years", "Определить возраст"),
            types.BotCommand("difference_between_dates", "Определить разницу между двумя датами"),
            types.BotCommand("discount", "Рассчитать скидку"),
            types.BotCommand("default_calculator", "Обычный калькулятор"),
            types.BotCommand("inline_calculator", "Инлайн калькулятор"),
            types.BotCommand("/cancel", "Отмена"),
            types.BotCommand("/help", "Справка"),
        ]
    )
