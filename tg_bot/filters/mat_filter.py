from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import BoundFilter, Filter


#from tg_bot.config import Config


class MatFilter(Filter):
    #key = 'mat_filter'
    mat_filter = ['хуй', 'хуйло', 'пезда', 'блять']

    # def __init__(self, mat_filter: list[str]):
    #     if isinstance(mat_filter, list):
    #         self.mat_filter = mat_filter

    async def check(self, message: types.message):
        return any(map(lambda x: x.lower() in self.mat_filter, message.text.split()))

# def register_filters(dp: Dispatcher):
#     dp.filters_factory.bind(MatFilter)