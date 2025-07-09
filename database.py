import logging
from redis.asyncio import Redis, ConnectionPool
from typing import Optional
from config_reader import config

connection_params = {
    'host': config.redis_host.get_secret_value(),
    'port': int(config.redis_port.get_secret_value()),
    'decode_responses': True,
    'username': config.redis_username.get_secret_value(),
    'password': config.redis_password.get_secret_value(),
    'protocol': 3
}
connection_pool = ConnectionPool(**connection_params)

async def get_file_id(filename: str) -> str|None:
    r = Redis().from_pool(connection_pool)
    file_id = await r.get(filename)
    await r.close()
    assert isinstance(file_id, Optional[str])
    return file_id

async def set_file_id(filename: str, file_id: str) -> bool:
    r = Redis().from_pool(connection_pool)
    try:
        await r.set(filename, file_id)
        success = True
    except Exception as e:
        logging.error(f'Error during insert to database: {e}')
        success = False
    finally:
        await r.close()
        return success