from loader import dp
from aiogram import types
import re
from main import has_cyrillic
from function import to_latin,to_cyrillic
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def change(message:types.Message):
    if has_cyrillic(message.text):
        print(message.text)
        print(to_latin(message.text))
        await message.answer(to_latin(message.text))
    else:
        await message.answer(to_cyrillic(message.text))