from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


async def bot_start(message: types.Message):
    await message.reply(f'Привіт {message.from_user.full_name}\n'
                        f'Твій id {message.from_user.id}\n'
                        f'Твій нікнейм {message.from_user.username if message.from_user.username else "відсутній"}\n'
                        f'Наявність преміум аккаунту: {"присутній" if message.from_user.is_premium else "відсутній"}')



def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
