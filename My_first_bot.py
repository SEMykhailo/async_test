from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="5471477552:AAE4Szgn46AaL3n0Tos1hDbAFFn8KXEF1iI")
dp = Dispatcher(bot)  #обробка вхідних повідомлень


@dp.message_handler(commands=['start'])   #декоратор для обробки повідомлень, фільтри і таке інше
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = f'Привіт {message.chat.first_name}\n' \
           f'Я буду повторяти за тобою твої наступні повідомлення'

    await bot.send_message(chat_id=chat_id, text=text)

@dp.message_handler()   #декоратор для обробки повідомлень, фільтри і таке інше
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = message.text

    await bot.send_message(chat_id=chat_id, text=text)

executor.start_polling(dp) #старт бота в режимі полінгу


