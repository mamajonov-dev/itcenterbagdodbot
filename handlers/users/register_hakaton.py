import sqlite3

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from states.register_hacaton import HacatonStata
from keyboards.default.mainmenubutoons import backbutton, genearatemainmenu
from keyboards.default.otherkeyboards import phonebutton
from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(text='🎁 Konkursga ro\'yxatdan o\'tish')
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

        await bot.send_message(chatid, 'Telefon nomeringizni jo\'nating ⬇️⬇️',
                               reply_markup=phonebutton())
        await HacatonStata.phone.set()


@dp.message_handler(state=HacatonStata.phone, content_types='contact')
async def getage(message: Message, state: FSMContext):
    chatid = message.chat.id
    first_name = message.contact.first_name
    phone = message.contact.phone_number
    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':
        await bot.send_message(chatid, 'Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        await state.update_data({'phone': message.text})
        await bot.send_message(-1002165970917, 'IT center Konkurs')
        await bot.send_contact(chat_id=-1002165970917, first_name=first_name, phone_number=phone)
        await bot.send_message(chatid, 'Qo\'shimcha telefon nomeringizni kiriting',
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
        phone = data['phone']
        phone = f'{phone}, {message.text}'
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
                    VALUES (?,?,?,?,?)''', (name, phone, age, sanab, chatid))
        database.commit()
        database.close()

        database = sqlite3.connect('database.sqlite')
        cursor = database.cursor()
        cursor.execute('''SELECT id, sana FROM quizusers WHERE chatid = ?''', (chatid,))
        user = cursor.fetchone()
        database.close()


        text = f"✅✅   QUIZ   ✅✅\nRo'yxatdan o'tgan: \n{text}\nYoshi: {age}\nTelefon: {message.text}\n\nID: {user[0]}\nSana: {sanab}"
        await bot.send_message(ADMINS[0], text)
        await bot.send_message(chatid,
                               f'Tabriklaymiz ro\'yxatdan o\'tdingiz ✅.\nSizning ID raqamingiz: {user[0]}\n\n Sizni "KONKURS" da kutib qolamiz. Konkurs o\'tkaziladigan sanasini kanlada e\'lon qilamiz. Kanalimizni kuzatib boring '
                               '\nBog\'lanish uchun +998917871199 +998998871199\nYoki telegram @NurmuhammadMamajonov',
                               reply_markup=genearatemainmenu())
        await state.finish()
