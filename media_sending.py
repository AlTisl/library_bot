from aiogram.types import Message, FSInputFile, ReplyMarkupUnion
from typing import Optional
from decorators import check_file_id_existing

@check_file_id_existing
async def send_image(msg: Message, file_path: str, keyboard: Optional[ReplyMarkupUnion] = None, *,
                     obj: Optional[str|FSInputFile] = None) -> Message:
    assert obj is not None
    return await msg.answer_photo(obj, reply_markup=keyboard)

@check_file_id_existing
async def send_doc(msg: Message, file_path: str, *, obj: Optional[str|FSInputFile] = None) -> Message:
    assert obj is not None
    return await msg.answer_document(obj)

@check_file_id_existing
async def send_animation(msg: Message, file_path: str, keyboard: Optional[ReplyMarkupUnion] = None, *,
                         obj: Optional[str|FSInputFile] = None) -> Message:
    assert obj is not None
    return await msg.answer_animation(obj, reply_markup=keyboard)