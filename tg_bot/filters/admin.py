from aiogram import Dispatcher
from aiogram.dispatcher.filters import BoundFilter


from tg_bot.config import Config


class AdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin = None):
        self.is_admin = is_admin

    async def check(self, obj):
        config: Config = obj.bot.get("config")
        user_id = obj.from_user.id
        return user_id in config.tg_bot.admin_ids

def register_filters_admin(dp: Dispatcher):
     dp.filters_factory.bind(AdminFilter)