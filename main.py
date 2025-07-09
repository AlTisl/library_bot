import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from config_reader import config
from database import connection_pool
from handlers import info, fsm_sources, fsm_repo, fsm_teachers, fsm_services
from redis.asyncio import Redis

# включаем логирование
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s')

async def main():
    bot = Bot(token=config.bot_token.get_secret_value(),
          default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    dp = Dispatcher(storage=RedisStorage(Redis().from_pool(connection_pool)))
    dp.include_routers(fsm_repo.router, fsm_teachers.router, fsm_sources.router,
                       fsm_services.router, info.router)

    await bot.delete_webhook(drop_pending_updates=True)     # сброс сообщений
    await dp.start_polling(bot)                             # ожидание поступления сообщений

if __name__ == '__main__':
    asyncio.run(main())