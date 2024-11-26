import sqlite3

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from states.register_hacaton import HacatonStata
from keyboards.default.mainmenubutoons import backbutton, genearatemainmenu
from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(text='🎁 Quizga ro\'yxatdan o\'tish')
async def comment(message: Message):
    chatid = message.chat.id
    await bot.send_message(chatid, 'Ilitmos ism va  familiyangizni kiriting.',
                           reply_markup=backbutton())
    await HacatonStata.name.set()


@dp.message_handler(state=HacatonStata.name)
async def getcomment(message: Message, state: FSMContext):
    chatid = message.chat.id
    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':

        await bot.send_message(chatid, 'Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        chat_id = message.chat.id
        fullname = message.from_user.full_name
        username = message.from_user.username
        user = message.from_user.get_mention()
        text = f'Ismi: {fullname}\n' \
               f'User name: @{username}\n' \
               f'Telegram id: {chat_id}\n' \
               f'User: {user}\n\n\n' \
               f'Ism familiyasi : \n{message.text}'
        await state.update_data(
            {'text': text, 'name': message.text}
        )
        await bot.send_message(chatid, text='Yoshngizni kiriting', reply_markup=backbutton())
        await HacatonStata.age.set()


@dp.message_handler(state=HacatonStata.age)
async def getage(message: Message, state: FSMContext):
    chatid = message.chat.id
    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':
        await bot.send_message(chatid, 'Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        await state.update_data({'age': message.text})

        await bot.send_message(chatid, 'Telefon nomeringizni kiriting',
                               reply_markup=backbutton())
        await HacatonStata.nomer.set()


@dp.message_handler(state=HacatonStata.nomer)
async def getphone(message: Message, state: FSMContext):
    chatid = message.chat.id
    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':
        await bot.send_message(chatid, 'Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        data = await state.get_data()
        text = data['text']
        age = data['age']
        name = data['name']
        database = sqlite3.connect('database.sqlite')
        cursor = database.cursor()
        cursor.execute('''SELECT sana FROM quizusers''')
        sana = cursor.fetchall()
        database.close()

        if len(sana) <= 27:
            sanab = 1
        else:
            sanab = 2
        database = sqlite3.connect('database.sqlite')
        cursor = database.cursor()
        cursor.execute('''INSERT INTO  quizusers(name, telefon, age, sana, chatid) 
                    VALUES (?,?,?,?,?)''', (name, message.text, age, sanab, chatid))
        database.commit()
        database.close()

        database = sqlite3.connect('database.sqlite')
        cursor = database.cursor()
        cursor.execute('''SELECT id, sana FROM quizusers WHERE chatid = ?''', (chatid,))
        user = cursor.fetchone()
        database.close()
        oy = user[1]
        kun = ''
        if oy == 1:
            kun = '30-noyabr'
        elif oy == 2:
            kun = '1-dekabr'
        text = f"✅✅   QUIZ   ✅✅\nRo'yxatdan o'tgan: \n{text}\nYoshi: {age}\nTelefon: {message.text}\n\nID: {user[0]}\nSana: {kun}"
        await bot.send_message(ADMINS[0], text)
        await bot.send_message(chatid,
                               f'Tabriklaymiz ro\'yxatdan o\'tdingiz ✅.\nSizning ID raqamingiz: {user[0]}\n\n {kun} kuni 10:00 da "QUIZ" da kutib qolamiz. '
                               '\nBog\'lanish uchun +998917871199\nYoki telegram @NurmuhammadMamajonov',
                               reply_markup=genearatemainmenu())
        await state.finish()
