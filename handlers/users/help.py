from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
import os
from loader import dp
admin = os.getenv('ADMINS')

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):

    if str(message.chat.id) == str(admin):
        text = ("Buyruqlar ro'yxati: ",
                "/start - Botni qayta ishga tushirish",
                "/help - Yordam",
                "/sendad - Reklama jo'natish")
    else:
        text = ("Buyruqlar ro'yxati: ",
                "/start - Botni qayta ishga tushirish",
                "/help - Yordam")
    await message.answer("\n".join(text))
