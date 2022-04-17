from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("default_calculator", "Обычный калькулятор"),
            types.BotCommand("inline_calculator", "Инлайн калькулятор"),
            types.BotCommand("/cancel", "Отмена"),
            types.BotCommand("/help", "Справка"),
        ]
    )
