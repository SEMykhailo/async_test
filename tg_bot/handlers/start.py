import re

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import get_start_link


async def bot_start_with_dp(message: types.Message):
    await message.answer(f"Ви передали  {message.get_args()}")


async def bot_start(message: types.Message):
    deep_link = await get_start_link(payload='12345')
    await message.answer(f"Hello {message.from_user.full_name} your link {deep_link}")




def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start_with_dp, CommandStart(deep_link=re.compile(r'\d{3,15}')))
    dp.register_message_handler(bot_start)