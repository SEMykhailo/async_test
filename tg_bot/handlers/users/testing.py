from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from tg_bot.states.test import Test


async def enter_test(message: types.Message):
    await message.answer('Ви почали тестування\n'
                         'Питання №1:\n'
                         'Скільки вам років?')

    await Test.Q1.set()


async def first_answer(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer('Питання №2:\n'
                         'Звідки ви?')
    await Test.next()


async def second_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer('Дякую за ваші відповіді')
    await message.answer(f'Тобі {answer1} років')
    await message.answer(f'Ти з {answer2}')

    await state.reset_state()

def register_testing(dp: Dispatcher):
    dp.register_message_handler(enter_test, Command('test'))
    dp.register_message_handler(first_answer, state=Test.Q1)
    dp.register_message_handler(second_answer, state=Test.Q2)
