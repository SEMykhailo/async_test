from aiogram import types


async def bot_echo(message: types.Message):
    text = [
        "Ехо без стану.",
        "Повідомлення:",
        message.text
    ]

     await message.answer('\n'.join(text))


async def bot_echo_all(message: types.Message, state: FSMCContext):
    state_name = await state.get_state()
    text = [
        f"Ехо в стані {hcode(state_name)}.",
        "Повідомлення:",
        message.text
    ]

     await message.answer('\n'.join(text))

def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state='*', content_types=types.ContentType.ANY)
