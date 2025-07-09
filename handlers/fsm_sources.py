from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from constants import keyboard_buttons as buttons, inline_buttons as inlines, paths
from keyboards import kb_sources, kb_catalog, kb_library, kb_repo
from media_sending import send_image, send_animation
import strings

class NetworkSources(StatesGroup):
    choosing_source = State()

router = Router()

@router.message(StateFilter(None), F.text.lower() == buttons.RESOURCES.lower())
async def source_section_choosed(message: Message, state: FSMContext):
    await message.answer(**strings.RESOURCES_TEXT.as_kwargs(), reply_markup=kb_sources)
    await state.set_state(NetworkSources.choosing_source)

@router.message(StateFilter(NetworkSources.choosing_source), F.text.lower() == buttons.CATALOG.lower())
async def catalog_as_source(message: Message, state: FSMContext):
    await send_image(message, paths.CATALOG_IMAGE, kb_catalog)

@router.message(StateFilter(NetworkSources.choosing_source), F.text.lower() == buttons.LIBRARY.lower())
async def library_as_source(message: Message, state: FSMContext):
    await send_animation(message, paths.LIBRARY_ANIMATION, kb_library)
    await message.answer(**strings.LIBRARY_TEXT.as_kwargs())

@router.message(StateFilter(NetworkSources.choosing_source), F.text.lower() == buttons.REPO.lower())
async def repo_as_source(message: Message, state: FSMContext):
    await send_animation(message, paths.REPO_ANIMATION, kb_repo)