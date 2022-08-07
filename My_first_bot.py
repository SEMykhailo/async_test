from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="5471477552:AAE4Szgn46AaL3n0Tos1hDbAFFn8KXEF1iI")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'Якийсь текст'

    await bot.send_message(chat_id=chat_id, text=text)


executor.start_polling(dp)
