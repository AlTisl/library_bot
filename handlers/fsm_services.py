from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from constants import keyboard_buttons as buttons, inline_buttons as inlines, paths
from keyboards import kb_services, kb_sources, kb_catalog, kb_library, kb_repo, kb_udk, kb_founds, kb_pre_order, kb_edd_mba
from media_sending import send_animation, send_image, send_doc
import strings

class ServiceCategories(StatesGroup):
    choosing_category = State()
    choosing_source = State()

router = Router()

@router.message(StateFilter(None), F.text.lower() == buttons.SERVICES.lower())
async def services_section_choosen(message: Message, state: FSMContext):
    await message.answer(**strings.PROMPT_TEXT.as_kwargs(), reply_markup=kb_services)
    await state.set_state(ServiceCategories.choosing_category)

# Пункт "Віртуальна довідка" не описан, т.к. он дублирует пункт из основного меню

@router.message(StateFilter(ServiceCategories.choosing_category),
                F.text.lower() == buttons.FIND_LIT.lower())
async def find_lit_category_choosen(message: Message, state: FSMContext):
    await message.answer(**strings.FIND_LIT_TEXT.as_kwargs(), reply_markup=kb_sources)
    await state.set_state(ServiceCategories.choosing_source)

@router.message(StateFilter(ServiceCategories.choosing_source), F.text.lower() == buttons.CATALOG.lower())
async def catalog_as_source(message: Message):
    await send_image(message, paths.CATALOG_IMAGE, kb_catalog)

@router.message(StateFilter(ServiceCategories.choosing_source), F.text.lower() == buttons.LIBRARY.lower())
async def library_as_source(message: Message):
    await send_animation(message, paths.LIBRARY_ANIMATION, kb_library)
    await message.answer(**strings.LIBRARY_TEXT.as_kwargs())

@router.message(StateFilter(ServiceCategories.choosing_source), F.text.lower() == buttons.REPO.lower())
async def repo_as_source(message: Message):
    await send_animation(message, paths.REPO_ANIMATION, kb_repo)

@router.message(StateFilter(ServiceCategories.choosing_source), Command('cancel'))
@router.message(StateFilter(ServiceCategories.choosing_source), F.text.lower() == buttons.CANCEL.lower())
async def cmd_cancel(message: Message, state: FSMContext):
    await services_section_choosen(message, state)

@router.message(StateFilter(ServiceCategories.choosing_category), F.text.lower() == buttons.FIND_UDK.lower())
async def udk_section_choosen(message: Message) -> None:
    await message.answer(**strings.UDK_TEXT.as_kwargs(), reply_markup=kb_udk)

@router.message(StateFilter(ServiceCategories.choosing_category), F.text.lower() == buttons.CONSULTATION.lower())
async def consultation_section_choosen(message: Message) -> None:
    await message.answer(**strings.CHAT_TEXT.as_kwargs())

@router.message(StateFilter(ServiceCategories.choosing_category), F.text.lower() == buttons.PRE_ORDER.lower())
async def pre_order_section_choosen(message: Message):
    await message.answer(**strings.FOUNDS_TEXT.as_kwargs(), reply_markup=kb_founds)
    await send_animation(message, paths.PRE_ORDER_ANIMATION, kb_pre_order)

@router.message(StateFilter(ServiceCategories.choosing_category), F.text.lower() == buttons.EDD_MBA.lower())
async def edd_mba_section_choosen(message: Message):
    await send_animation(message, paths.EDD_MBA_ANIMATION, kb_edd_mba)
    await message.answer(**strings.EDD_MBA_TEXT.as_kwargs())