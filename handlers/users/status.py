from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp,Command

from api import get_users
from loader import dp
@dp.message_handler(Command('info'))
async def info(message:types.Message):
    text = "🤖Botga qaysi yozuvda kiritishizni aytishingiz shart emas.Bot o'zi aniqlab oladi! \n" \
           "1️⃣.Bu bot orqali <b>Lotindan Krillga</b> aksincha <b>Krilldan Lotinga</b> o'girishga yordam beradi!\n" \
           "2️⃣.<b>Word(docx)</b> fayllarni ham o'girishingiz mumkin!\n" \
           "❗️ Faqatgina <b>.docx</b> fayllarni o'giradi bot(hozircha😉)\n" \
           "📝 Shunchaki so'z yozing yoki 📄 Fayl yuklang!"
    await message.reply(text)
@dp.message_handler(Command('status'))
async def get(message:types.Message):
    text = get_users()
    await message.answer(text)

