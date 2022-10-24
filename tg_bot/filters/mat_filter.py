from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import BoundFilter


#from tg_bot.config import Config


class MatFilter(BoundFilter):
    mat_list = ['хуй', 'хуйло', 'пезда', 'блять']

    async def check(self, message: types.message):
        return any(map(lambda x: x.lower() in self.mat_list, message.text.split()))

def register_filters(dp: Dispatcher):
    dp.filters_factory.bind(MatFilter)