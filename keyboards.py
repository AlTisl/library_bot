from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
import constants.keyboard_buttons as buttons
import constants.inline_buttons as inlines

def get_reply_keyboard(*buttons: list[str]) -> ReplyKeyboardMarkup:
    kb = [[KeyboardButton(text=btn) for btn in row] for row in buttons]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_inline_keyboard(*buttons: dict[str, str]) -> InlineKeyboardMarkup:
    kb = [[InlineKeyboardButton(**locals()|btn) for btn in buttons]]
    return InlineKeyboardMarkup(inline_keyboard=kb)

# "Обычные" кнопки
kb_common = get_reply_keyboard(
    [buttons.CATALOG, buttons.SITE, buttons.REPO],
    [buttons.HELP, buttons.UDK, buttons.CHAT],
    [buttons.FOR_TEACHERS, buttons.FOR_STUDENTS, buttons.LIT_TREASURE],
    [buttons.SCHEDULE, buttons.RESOURCES, buttons.SERVICES]
)
kb_repo_base = get_reply_keyboard(
    [buttons.RECOMENDATIONS, buttons.STUD_WORK],
    [buttons.MONOGRAPH, buttons.TEXTBOOK, buttons.ARTICLE],
    [buttons.CANCEL]
)
kb_teachers = get_reply_keyboard(
    [buttons.PRE_ORDER, buttons.AVAILABILITY],
    [buttons.PROFILE,  buttons.DATABASES],
    [buttons.SUPPORT, buttons.SEMINAR],
    [buttons.CANCEL]
)
kb_support = get_reply_keyboard(
    [buttons.ZVO, buttons.REGISTRY, buttons.TCS],
    [buttons.CANCEL]
)
kb_sources = get_reply_keyboard(
    [buttons.CATALOG, buttons.LIBRARY, buttons.REPO],
    [buttons.CANCEL]
)
kb_services = get_reply_keyboard(
    [buttons.FIND_LIT, buttons.FIND_UDK, buttons.CONSULTATION],
    [buttons.PRE_ORDER, buttons.EDD_MBA, buttons.HELP],
    [buttons.CANCEL]
)

# Инлайн-кнопки
kb_help = get_inline_keyboard(inlines.HELP_ORDER, inlines.SOCIAL)
kb_udk = get_inline_keyboard(inlines.HELP)
kb_lit_treasure = get_inline_keyboard(inlines.LIT_TREASURE)
kb_catalog = get_inline_keyboard(inlines.CATALOG)
kb_site = get_inline_keyboard(inlines.SITE)
kb_library = get_inline_keyboard(inlines.LIBRARY)
kb_repo = get_inline_keyboard(inlines.REPO)
kb_repo1 = get_inline_keyboard(inlines.REPO1)
kb_founds = get_inline_keyboard(inlines.FOUNDS)
kb_pre_order = get_inline_keyboard(inlines.PRE_ORDER)
kb_edd_mba = get_inline_keyboard(inlines.EDD_MBA)
kb_statute = get_inline_keyboard(inlines.STATUTE)
kb_registry = get_inline_keyboard(inlines.REGISTRY)