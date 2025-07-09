from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from constants import keyboard_buttons as buttons, inline_buttons as inlines, paths
from keyboards import kb_teachers, kb_founds, kb_pre_order, kb_support, kb_statute, kb_registry
from media_sending import send_animation, send_image, send_doc
import strings

class TeacherCategories(StatesGroup):
    choosing_category = State()
    choosing_publications_support = State()

router = Router()

@router.message(StateFilter(None), F.text.lower() == buttons.FOR_TEACHERS.lower())
async def teachers_section_choosen(message: Message, state: FSMContext):
    await message.answer(**strings.PROMPT_TEXT.as_kwargs(), reply_markup=kb_teachers)
    await state.set_state(TeacherCategories.choosing_category)

@router.message(StateFilter(TeacherCategories.choosing_category),
                F.text.lower() == buttons.PRE_ORDER.lower())
async def pre_order_category_choosen(message: Message):
    await message.answer(**strings.FOUNDS_TEXT.as_kwargs(), reply_markup=kb_founds)
    await send_animation(message, paths.PRE_ORDER_ANIMATION, kb_pre_order)

@router.message(StateFilter(TeacherCategories.choosing_category),
                F.text.lower() == buttons.AVAILABILITY.lower())
async def availability_category_choosen(message: Message):
    await message.answer(**strings.AVAILABILITY_TEXT.as_kwargs())

@router.message(StateFilter(TeacherCategories.choosing_category),
                F.text.lower() == buttons.PROFILE.lower())
async def profile_category_choosen(message: Message):
    await send_image(message, paths.PROFILE_IMAGE)
    await message.answer(**strings.PROFILE_TEXT.as_kwargs())
    await send_image(message, paths.GOOGLE_SCHOLAR_IMAGE)
    await send_image(message, paths.ORCID_IMAGE)

@router.message(StateFilter(TeacherCategories.choosing_category),
                F.text.lower() == buttons.DATABASES.lower())
async def databases_category_choosen(message: Message, state: FSMContext):          # не реализовано
    pass

@router.message(StateFilter(TeacherCategories.choosing_category),
                F.text.lower() == buttons.SUPPORT.lower())
async def support_category_choosen(message: Message, state: FSMContext):
    await message.answer(**strings.SUPPORT_TEXT.as_kwargs(), reply_markup=kb_support)
    await state.set_state(TeacherCategories.choosing_publications_support)

@router.message(StateFilter(TeacherCategories.choosing_category),
                F.text.lower() == buttons.SEMINAR.lower())
async def seminar_category_choosen(message: Message, state: FSMContext):          # не реализовано
    pass

@router.message(StateFilter(TeacherCategories.choosing_publications_support), Command('cancel'))
@router.message(StateFilter(TeacherCategories.choosing_publications_support),
                F.text.lower() == buttons.CANCEL.lower())
async def cmd_cancel(message: Message, state: FSMContext):
    await teachers_section_choosen(message, state)

@router.message(StateFilter(TeacherCategories.choosing_publications_support),
                F.text.lower() == buttons.ZVO.lower())
async def zvo_subcategory_choosen(message: Message):
    await send_image(message, paths.ATTENTION_IMAGE)
    await message.answer(**strings.ZVO_TXT.as_kwargs(), reply_markup=kb_statute)

@router.message(StateFilter(TeacherCategories.choosing_publications_support),
                F.text.lower() == buttons.REGISTRY.lower())
async def registry_subcategory_choosen(message: Message):
    await send_animation(message, paths.REGISTRY_ANIMATION)
    await message.answer(**strings.REGISTRY_TEXT.as_kwargs(), reply_markup=kb_registry)

@router.message(StateFilter(TeacherCategories.choosing_publications_support),
                F.text.lower() == buttons.TCS.lower())
async def tcs_subcategory_choosen(message: Message):
    await message.answer(**strings.TCS_TEXT.as_kwargs())
    await send_doc(message, paths.TCS_BOOKLET)