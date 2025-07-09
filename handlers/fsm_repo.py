from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from constants import keyboard_buttons as buttons, paths
from keyboards import kb_repo_base, kb_repo1
from media_sending import send_doc
import strings

class RepoTemplates(StatesGroup):
    choosing_template = State()

router = Router()

templates = {
    buttons.RECOMENDATIONS: paths.RECOMENDATIONS,
    buttons.STUD_WORK: paths.STUD_WORK,
    buttons.TEXTBOOK: paths.TEXTBOOK,
    buttons.ARTICLE: paths.ARTICLE,
    buttons.MONOGRAPH: paths.MONOGRAPH
}

@router.message(StateFilter(None), F.text.lower() == buttons.REPO.lower())
async def repo_section_choosed(message: Message, state: FSMContext):
    await message.answer(**strings.REPO_1_TEXT.as_kwargs(), reply_markup=kb_repo1)
    await message.answer(**strings.REPO_MAIL_TEXT.as_kwargs())
    await message.answer(**strings.REPO_2_TEXT.as_kwargs(), reply_markup=kb_repo_base)
    await state.set_state(RepoTemplates.choosing_template)

@router.message(StateFilter(RepoTemplates.choosing_template),
                F.text.lower().in_([t.lower() for t in templates.keys()]),
                F.text.lower().as_('template'))
async def template_choosed(message: Message, template: str):
    templates_lower = {key.lower(): value for key, value in templates.items()}
    path = templates_lower.get(template)
    assert path is not None
    await send_doc(message, path)