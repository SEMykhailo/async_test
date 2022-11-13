from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command, state

from tg_bot.filters.mat_filter import MatFilter

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

async def bot_start(message: types.Message):
    await message.answer(f'Для того, щоб дізнатися свій Telegram id введіть команду /info\n'
                         f'Також цей бот може провести маленьке тестування, для цього введіть команду /test\n'
                         f'Крім цього, його можна використовувати, як мат фільтр в чатах, але кількість матів дуже обмежена і це реалізовано просто для тестування фільтрів бота')

    #await state.reset_state()

#commit
async def  give_id_stickers(message: types.Message):
    await message.answer(message.sticker.file_id)

def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, Command('start'), state='*')
    dp.register_message_handler(bot_info, Command('info'))
    dp.register_message_handler(give_id_stickers, content_types=['sticker'])
    dp.register_message_handler(bot_filter_pytin, Text(contains=FORBIDDEN_PHRASE_1, ignore_case=True))
    dp.register_message_handler(bot_filter_mat, MatFilter())