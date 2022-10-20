from aiogram import types, Dispatcher


async def bot_start(message: types.Message):
    bot = message.bot
    chat_id = message.chat.id
    text = message.text

    await bot.send_message(chat_id=chat_id, text=text)

async def bot_user(message: types.Message):
    await message.reply(text=message.text)

def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_start, text="/start")
    dp.register_message_handler(bot_user)