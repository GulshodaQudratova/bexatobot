import logging
from aiogram import types

from api import create_user
from data.config import CHANNELS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import bot, dp
from data.config import CHANNELS
from utils.misc import subscription
@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    user = message.from_user.id
    name = message.from_user.full_name
    create_user(name=name,telegram_id=user)
    final_status = True
    btn = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        status = await subscription.check(user_id=user,
                                          channel=channel)
        final_status *= status
        channel = await bot.get_chat(channel)
        if status:
            invite_link = await channel.export_invite_link()
            btn.add(InlineKeyboardButton(text=f"✅ {channel.title}", url=invite_link))
        if not status:
            invite_link = await channel.export_invite_link()
            btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))
    btn.add(InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs"))
    if final_status:
        text = "🤖Botga qaysi yozuvda kiritishizni aytishingiz shart emas.Bot o'zi aniqlab oladi! \n" \
               "1️⃣.Bu bot orqali <b>Lotindan Krillga</b> aksincha <b>Krilldan Lotinga</b> o'girishga yordam beradi!\n" \
               "2️⃣.<b>Word(docx)</b> fayllarni ham o'girishingiz mumkin!\n" \
               "❗️ Faqatgina <b>.docx</b> fayllarni o'giradi.\n" \
               "📝 Shunchaki so'z yozing yoki 📄 Fayl yuklang!"
        await message.answer(text)
    if not final_status:
        await message.answer( "👋 Assalomu alaykum\n" +"Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling!", disable_web_page_preview=True, reply_markup=btn)
@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    btn = InlineKeyboardMarkup()
    final_status = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        final_status *=status
        channel = await bot.get_chat(channel)
        if not status:
            invite_link = await channel.export_invite_link()
            btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))

    btn.add(InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs"))
    if final_status:
        text = "🤖Botga qaysi yozuvda kiritishizni aytishingiz shart emas.Bot o'zi aniqlab oladi! \n" \
               "1️⃣.Bu bot orqali <b>Lotindan Krillga</b> aksincha <b>Krilldan Lotinga</b> o'girishga yordam beradi!\n" \
               "2️⃣.<b>Word(docx)</b> fayllarni ham o'girishingiz mumkin!\n" \
               "❗️ Faqatgina <b>.docx</b> fayllarni o'giradi bot(hozircha😉)\n" \
               "📝 Shunchaki so'z yozing yoki 📄 Fayl yuklang!"
        await call.message.answer(text)
    if not final_status:
        await call.answer(cache_time=60)
        await call.message.answer("Siz quyidagi kanal(lar)ga obuna bo'lmagansiz!",reply_markup=btn)
        await call.message.delete()
