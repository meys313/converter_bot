from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("/cancel", "Отмена действия / Выход из команды"),
            types.BotCommand("/command", "Список команд"),
        ]
    )
