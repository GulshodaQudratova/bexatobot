import aiogram.utils.exceptions

from loader import dp,bot
from aiogram import types
from api import get_users
import asyncio
from environs import Env
env = Env()
env.read_env()
id = env.str('ADVERTISING_CHANNEL')
@dp.channel_post_handler(content_types=types.ContentTypes.ANY)
async def reklama(message:types.Message):
    channel_id =id
    message_id = message.message_id
    users = get_users()
    for user in users:
        try:
            await bot.forward_message(chat_id=user['telegram_id'],from_chat_id=channel_id,message_id=message_id)
            asyncio.sleep(2)
        except aiogram.utils.exceptions.BotBlocked:
            print('Blocked')
        except Exception as e:
            print(e)
