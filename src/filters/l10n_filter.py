from aiogram.filters import BaseFilter
from aiogram.types import Message
from fluent.runtime import FluentLocalization

class L10nTextFilter(BaseFilter):
    def __init__(self, key: str):
        self.key = key

    async def __call__(self, message: Message, l10n: FluentLocalization) -> bool:
        expected = l10n.format_value(self.key)
        return message.text == expected
