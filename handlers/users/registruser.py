from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import *
from data.config import *

from keyboards.default.cousesbuttons import *
from keyboards.default.otherkeyboards import *
from keyboards.default.mainmenubutoons import *
from states.registruserstate import *


@dp.message_handler(text='📝 Kurslarga ro\'yxatdan o\'tish')
async def registr(message: Message):
    await message.answer('Kursni tanlang', reply_markup=generatecoursebuttons())
    await RegistrUserState.course.set()


@dp.message_handler(state=RegistrUserState.course)
async def getcoursename(message: Message, state: FSMContext):
    text = message.text
    if text == '⬅️ Orqaga' or text == '/start' or text == '/help':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        await message.answer('Ism, familiya va yoshingizni kiritng', reply_markup=backbutton())
        await state.update_data({'course': text})
        await RegistrUserState.name.set()


@dp.message_handler(state=RegistrUserState.name)
async def getcoursename(message: Message, state: FSMContext):
    text = message.text
    if text == '⬅️ Orqaga' or text == '/start' or text == '/help':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:

        await message.answer('Telefon raqamingizni kiriting. "+" belgisisiz:\n'
                             'Namuna: 998911234567', reply_markup=backbutton())
        await state.update_data({'name': text})
        await RegistrUserState.phone.set()


@dp.message_handler(state=RegistrUserState.phone)
async def getcoursename(message: Message, state: FSMContext):
    text = message.text
    if text == '⬅️ Orqaga' or text == '/start' or text == '/help':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        if text.isdigit():

            await message.answer('Qo\'shimcha telefon raqamingizni kiriting "+" belgisisiz.\n'
                                 'Namuna: 998911234567', reply_markup=backbutton())
            await state.update_data({'phone': text})
            await RegistrUserState.phone2.set()
        else:
            await message.answer('❗️Faqat raqam kiriting!!!\nNamuna: 998911234567')


@dp.message_handler(state=RegistrUserState.phone2)
async def getcoursename(message: Message, state: FSMContext):
    text = message.text
    if text == '⬅️ Orqaga' or text == '/start' or text == '/help':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        if text.isdigit():
            await state.update_data({'phone2': text})
            data = await state.get_data()
            course = data['course']
            name = data['name']
            phone = data['phone']
            phone2 = data['phone2']
            user = message.from_user.get_mention()
            senduser = f"❗️Yangi o'quvchi\n" \
                       f"User: {user}\n" \
                       f"Student: {name}\n" \
                       f"Kurs: {course}\n" \
                       f"\nTelefon: {phone}\n" \
                       f"Qo'shimcha: {phone2}"
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=senduser)
            await message.answer("✅ Ma'lumotingiz qabul qilindi. Menejerimiz tez orada siz bilan bog'lanadi! \n"
                                 "Bizning kurslarni tanlaganingiz uchun raxmat! ", reply_markup=genearatemainmenu())
            await state.finish()
        else:
            await message.answer('❗️Faqat raqam kiriting!!!\nNamuna: 998911234567')
