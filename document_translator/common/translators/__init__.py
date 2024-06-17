from enum import Enum
from typing import Callable

from .open_ai_translator import translate as open_ai_translate


class Translator(str, Enum):
    openai = "openai"


def get_translator(translator: str) -> Callable[[list[str], str, str], list[str]]:
    if translator == Translator.openai:
        return open_ai_translate
    raise ValueError("Invalid translator")
