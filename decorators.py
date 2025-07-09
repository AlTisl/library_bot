from aiogram.types import Message, FSInputFile
from database import get_file_id, set_file_id
from os.path import basename
from typing import Callable

def check_file_id_existing(func: Callable) -> Callable:
    async def wrapper(*args, **kwargs) -> Message:
        path = kwargs.get('file_path') or args[1]
        obj_name = basename(path)
        obj_id = await get_file_id(obj_name)
        if obj_id is not None:
            return await func(*args, **kwargs, obj=obj_id)
        else:
            result = await func(*args, **kwargs, obj=FSInputFile(path))
            if result.photo is not None:
                mt = result.photo[-1]
            else:
                mt = result.document or result.animation
            await set_file_id(obj_name, mt.file_id)
            return result
    return wrapper
