import random

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command, state

from tg_bot.filters.mat_filter import MatFilter
from tg_bot.keyboards.kb_start import kb

FORBIDDEN_PHRASE_1 = [
    'Путін',
    'хуйло',
]
async def bot_info(message: types.Message):
    await message.reply(f'Привіт {message.from_user.full_name}\n'
                        f'Твій id {message.from_user.id}\n'
                        f'Твій нікнейм {message.from_user.username if message.from_user.username else "відсутній"}\n'
                        f'Наявність преміум аккаунту: {"присутній" if message.from_user.is_premium else "відсутній"}')

async def bot_filter_mat(message: types.Message):
    await message.reply(f'Не можна такого говорити')

async def bot_filter_pytin(message: types.Message):
    await message.reply(f'Підтримую')

async def bot_about(message: types.Message):
    await message.answer(f'Для того, щоб дізнатися свій Telegram id введіть команду /info\n'
                        f'Також цей бот може провести маленьке тестування, для цього введіть команду /test\n'
                        f'Для того, щоб получити id стікера - просто відправте його в чат\n'
                        f'Якщо хочете получити випадковий стікер з котиком введіть команду /give\n'
                        f'Крім цього, його можна використовувати, як мат фільтр в чатах, але кількість матів дуже обмежена і це реалізовано просто для тестування фільтрів бота')

async def bot_start(message: types.Message):
    await message.bot.send_message(chat_id=message.chat.id, text='Привіт', reply_markup=kb)

    #await state.reset_state()

async def give_cat_sticker(message: types.Message):
    STICKER_ID = ['CAACAgIAAxkBAAIBHWNxIcTBQAGIYAkd6ck4PgS3KKKTAAJqAQACFnxoAwWaR4EyB72cKwQ',
                  'CAACAgIAAxkBAAIBH2NxIlsTQUEOGrpRRzcAAcEceVqB2AACKg8AAmrdSUqUayj3S1F61isE',
                  'CAACAgIAAxkBAAIBIWNxIl2MuEYtqymUav3kTOPB7J8fAALjCAACXAJlA1UDiUYLzAqHKwQ',
                  'CAACAgIAAxkBAAIBI2NxImCUiDxTIIpwAWLVOi7pF8iVAAL5CQACFRdZSiAiPE2yrwo1KwQ',
                  'CAACAgUAAxkBAAIBJWNxImTgmH7iS8snnkGTcJUcx5LHAAKGAgACmLa8LxZxhWGi_gPmKwQ']
    id_sticker = random.choice(STICKER_ID)
    await message.bot.send_sticker(message.from_user.id, sticker=id_sticker)

async def  give_id_stickers(message: types.Message):
    await message.answer(message.sticker.file_id)

def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, Command('start'), state='*')
    dp.register_message_handler(bot_info, Command('info'))
    dp.register_message_handler(give_cat_sticker, Command("give"))
    dp.register_message_handler(bot_about, Command('about'))
    dp.register_message_handler(give_id_stickers, content_types=['sticker'])
    dp.register_message_handler(bot_filter_pytin, Text(contains=FORBIDDEN_PHRASE_1, ignore_case=True))
    dp.register_message_handler(bot_filter_mat, MatFilter())