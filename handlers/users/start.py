from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3
from utils.misc.subscription import check
from data.config import CHANNELS
from keyboards.default.mainmenubutoons import genearatemainmenu
from loader import dp
from keyboards.default.otherkeyboards import channelbuuton


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.chat.id
    fullname = message.from_user.full_name
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! \nBagdad IT Academy telegram botiga xush kelibsiz")
    database = sqlite3.connect('././database.sqlite')
    cursor = database.cursor()
    try:
        cursor.execute('''INSERT INTO users(name, chatid)
        VALUES (?, ?)''', (fullname, chat_id))
        database.commit()
        database.close()
    except:
        database.close()
        pass
    channel = CHANNELS
    status = await check(user_id=message.from_user.id, channel=channel)
    if status:
        await message.answer('Hush kelibsiz', reply_markup=genearatemainmenu())
    else:
        await message.answer('Botdan foydalanish uchun telegram kanalimizga obuna bo\'ling. Va botni qayta ishga tushiring.', reply_markup=channelbuuton())
