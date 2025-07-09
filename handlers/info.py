from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from constants import keyboard_buttons as buttons, paths
from keyboards import kb_common, kb_catalog, kb_help, kb_site, kb_lit_treasure, kb_udk
from media_sending import send_image, send_doc, send_animation
import strings

router = Router()

@router.message(Command('start'))               # обработчик команды "старт"
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    assert message.from_user is not None
    await send_image(message, paths.START_IMAGE)
    await message.answer(**strings.greetings(message.from_user.full_name).as_kwargs())
    await send_doc(message, paths.BOOKLET)
    await message.answer(strings.READY_TEXT, reply_markup=kb_common)

@router.message(Command('cancel'))              # Обработчик команды "Отмена"
@router.message(F.text.lower() == buttons.CANCEL.lower())
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(strings.READY_TEXT, reply_markup=kb_common)

@router.message(F.text.lower() == buttons.HELP.lower())
async def help_section_choosen(message: Message) -> None:
    await send_animation(message, paths.HELP_ANIMATION)
    await message.answer(**strings.HELP_TEXT.as_kwargs(), reply_markup=kb_help)

@router.message(F.text.lower() == buttons.UDK.lower())
async def udk_section_choosen(message: Message) -> None:
    await message.answer(**strings.UDK_TEXT.as_kwargs(), reply_markup=kb_udk)

@router.message(F.text.lower() == buttons.CHAT.lower())
async def chat_section_choosen(message: Message) -> None:
    await message.answer(**strings.CHAT_TEXT.as_kwargs())

@router.message(F.text.lower() == buttons.SCHEDULE.lower())
async def schedule_section_choosen(message: Message) -> None:
    await message.answer(**strings.SCHEDULE_TEXT.as_kwargs())

@router.message(F.text.lower() == buttons.LIT_TREASURE.lower())
async def studies_section_choosen(message: Message) -> None:
    await send_image(message, paths.LIT_TREASURE_IMAGE, kb_lit_treasure)

@router.message(F.text.lower() == buttons.CATALOG.lower())
async def catalog_section_choosen(message: Message) -> None:
    await send_image(message, paths.CATALOG_IMAGE, kb_catalog)

@router.message(F.text.lower() == buttons.SITE.lower())
async def site_section_choosen(message: Message) -> None:
    await send_image(message, paths.SITE_IMAGE, kb_site)