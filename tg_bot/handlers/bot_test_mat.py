from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text

from tg_bot.filters.mat_filter import MatFilter

FORBIDDEN_PHRASE_1 = [
    'Путін',
    'хуйло',
]
async def bot_start(message: types.Message):
    await message.reply(f'Привіт {message.from_user.full_name}\n'
                        f'Твій id {message.from_user.id}\n'
                        f'Твій нікнейм {message.from_user.username if message.from_user.username else "відсутній"}\n'
                        f'Наявність преміум аккаунту: {"присутній" if message.from_user.is_premium else "відсутній"}')

async def bot_filter_mat(message: types.Message):
    await message.reply(f'Не можна такого говорити')

async def bot_filter_pytin(message: types.Message):
    await message.reply(f'Підтримую')

def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_filter_pytin, Text(contains=FORBIDDEN_PHRASE_1, ignore_case=True))
    dp.register_message_handler(bot_filter_mat, MatFilter())