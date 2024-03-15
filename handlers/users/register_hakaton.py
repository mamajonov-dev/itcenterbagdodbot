from aiogram.types import Message, InputFile
from aiogram.dispatcher import FSMContext

from states.register_hacaton import HacatonStata
from keyboards.default.mainmenubutoons import backbutton, genearatemainmenu
from data.config import ADMINS
from loader import dp, bot
from keyboards.default.otherkeyboards import hacatontest


@dp.message_handler(text='🎁 Musobaqaga (hacatonga) ro\'yxatdan o\'tish')
async def comment(message: Message):
    await message.answer('Ilitmos ism, familiya, yoshinginzni va telefon nomeringizni kiriting.', reply_markup=backbutton())
    await HacatonStata.name.set()

@dp.message_handler(state=HacatonStata.name)
async def getcomment(message: Message, state: FSMContext):
    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
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
               f'Ism familiyasi telefon nomeri: \n\n{message.text}'
        await state.update_data(
            {'text': text}
        )
        photo = InputFile('pythontest.jpeg')
        await message.answer_photo(photo=photo,caption='Pythonda masalani yeching. Javoblarini pastdagi variantlardan birini tanlang', reply_markup=hacatontest())
        await HacatonStata.python_test.set()

@dp.message_handler(state=HacatonStata.python_test)
async def getphone(message: Message, state: FSMContext):
    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:
        test = message.text
        data = await state.get_data()
        text = data['text']

        if test == '27':
            text = f"✅✅✅✅✅✅✅✅\nRo'yxatdan o'tgan: \n{text}"
            await bot.send_message(ADMINS[0], text)
            await message.answer('Tabriklaymiz ro\'yxatdan o\'tdingiz ✅.\n\n 20-mart kuni HAKATONda kutib qolamiz. \nBog\'lanish uchun +998917871199\nYoki telegram @NurmuhammadMamajonov',
                                 reply_markup=genearatemainmenu())
            await state.finish()
        else:
            await message.answer("Javobingiz noto'g'ri. Ro'yxatdan o'ta olmadingiz ❌", reply_markup=genearatemainmenu())
            text = f"❌❌❌❌❌❌❌\nRo'yxatdan o'tgan: \n{text}"
            await bot.send_message(ADMINS[0], text)
            await state.finish()