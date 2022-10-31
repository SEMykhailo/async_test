from aiogram.dispatcher.filters import BoundFilter


from tg_bot.config import Config


class AdminFilter(BoundFilter):
    key = "is_admin"

    async def check(self, obj):
        config: Config = obj.bot.get("config")
        user_id = obj.from_user.id
        return user_id in config.tg_bot.admin_ids

