from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3

from keyboards.default.mainmenubutoons import genearatemainmenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.chat.id
    fullname = message.from_user.full_name
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! \nIT Center Bag'dod (BUIC) telegram botiga xush kelibsiz", reply_markup=genearatemainmenu())
    database = sqlite3.connect('././database.sqlite')
    cursor = database.cursor()
    try:
        cursor.execute('''INSERT INTO users(fullname, telegram_id)
        VALUES (?, ?)''', (fullname, chat_id))
        database.commit()
        database.close()
    except:
        database.close()
        pass

