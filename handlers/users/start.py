from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}! Это конвертер бот. \n"
                         f"Вот список комманд по которым ты можешь обратиться к нему: \n\n"
                         f"<b>Отмена действия / Выход из команды</b> - /cancel \n\n"
                         f"<b>Конвертер валют 💰</b> - /currency \n\n"
                         f"<b>Перевод из одной системы счисления в другую 💻</b> - /scale_of_notation \n\n"
                         f"<b>Определить возраст человека по дате его рождения 🎉</b> - /detect_years \n\n"
                         f"<b>Определить разницу между двумя датами 📆</b> - /difference_between_dates \n\n"
                         f"<b>Конвертер единиц измерения температуры 🌡</b> - /temperature \n\n"
                         f"<b>Конвертер единиц измерения длины 📐</b> - /length \n\n"
                         f"<b>конвертер массы ⚖</b> - /weight \n\n"
                         f"<b>конвертер времени ⌛</b> - /time \n\n"
                         f"<b>конвертер единиц измерения кол-ва информации 📊</b> - /data_converter \n\n"
                         f"<b>рассчитать скидку 💯</b> - /discount \n\n"
                         f"<b>обычный калькулятор 📚</b> - /default_calculator \n\n"
                         f"<b>инлайн калькулятор 📚</b> - /inline_calculator \n\n"
                         f"<b>список команд</b> - /command \n\n"

                         )

