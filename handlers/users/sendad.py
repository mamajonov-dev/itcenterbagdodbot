import json

from aiogram.types import Message
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv
load_dotenv()
import os

from keyboards.default.mainmenubutoons import backbutton, genearatemainmenu
from keyboards.default.otherkeyboards import generateconfirmbutton
from loader import dp, bot
from states.sendadstates import SendadState

admin = os.getenv('ADMINS')

@dp.message_handler(commands='sendad')
async def senad(message: Message):
    if str(message.chat.id) == str(admin):
        await message.answer('Reklamani yozing: ', reply_markup=backbutton())
        await SendadState.ad.set()
    else:
        pass

@dp.message_handler(state=SendadState.ad, content_types=['photo', 'text'])
async def getad(message: Message, state: FSMContext):

    text = message.text
    if text == '⬅️ Orqaga':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    elif message.text:
        # data =  {"message_id": 3956, "from": {"id": 659237008, "is_bot": False, "first_name": "Nurmuhammad", "username": "NurmuhammadMamajonov", "language_code": "ru", "is_premium": True}, "chat": {"id": 659237008, "first_name": "Nurmuhammad", "username": "NurmuhammadMamajonov", "type": "private"}, "date": 1737709765, "photo": [{"file_id": "AgACAgIAAxkBAAIPY2eTWFFmzoQXqo25jfG23cLJa4CSAAL85zEbrnKQSKzDRCmu0sCoAQADAgADcwADNgQ", "file_unique_id": "AQAD_OcxG65ykEh4", "file_size": 2499, "width": 90, "height": 90}, {"file_id": "AgACAgIAAxkBAAIPY2eTWFFmzoQXqo25jfG23cLJa4CSAAL85zEbrnKQSKzDRCmu0sCoAQADAgADbQADNgQ", "file_unique_id": "AQAD_OcxG65ykEhy", "file_size": 38891, "width": 320, "height": 320}, {"file_id": "AgACAgIAAxkBAAIPY2eTWFFmzoQXqo25jfG23cLJa4CSAAL85zEbrnKQSKzDRCmu0sCoAQADAgADeQADNgQ", "file_unique_id": "AQAD_OcxG65ykEh-", "file_size": 162758, "width": 1024, "height": 1024}, {"file_id": "AgACAgIAAxkBAAIPY2eTWFFmzoQXqo25jfG23cLJa4CSAAL85zEbrnKQSKzDRCmu0sCoAQADAgADeAADNgQ", "file_unique_id": "AQAD_OcxG65ykEh9", "file_size": 163367, "width": 800, "height": 800}]}
        #
        # with open('json.json', mode='a') as  file:
        #     json.dump(data, file, indent=4, ensure_ascii=False)

        await state.update_data({'ad': text})
        await message.answer('Tasdiqlash: Jo\'natilsinmi?', reply_markup=generateconfirmbutton())
        await SendadState.resquest.set()
    elif message.photo:
        await state.update_data(
            {'ad': message.photo, 'caption': message.caption}
        )
        await message.answer('Tasdiqlash: Jo\'natilsinmi?', reply_markup=generateconfirmbutton())
        await SendadState.resquest.set()


@dp.message_handler(state=SendadState.resquest)
async def getimage(mesasge: Message, state: FSMContext):
    if mesasge.text == 'Ha':
        data = await state.get_data()
        text = data['ad']

        database = sqlite3.connect('././database.sqlite')
        cursor = database.cursor()
        cursor.execute('''SELECT chatid FROM users''')
        users = cursor.fetchall()
        print(type(text))

        for user in users:
            chat_id = user[0]
            if type(text) == str:
                await bot.send_message(chat_id, text, reply_markup=genearatemainmenu())
            elif type(text) == list:
                await bot.send_photo(chat_id, photo=text[0]['file_id'], caption=data['caption'], reply_markup=genearatemainmenu())
        await state.finish()
    elif mesasge.text == "Yo'q" or mesasge.text == '/start':
        await mesasge.answer('Bekor qilindi', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        await mesasge.answer('Variantlardan birini tanlang', reply_markup=generateconfirmbutton())


