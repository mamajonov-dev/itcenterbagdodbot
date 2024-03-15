from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from states.comments import Commentstate
from keyboards.default.mainmenubutoons import backbutton, genearatemainmenu
from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(text='📝 Fikr va takliflar')
async def comment(message: Message):
    await message.answer('Fikr va takliflaringizni bitta matnda izohlang:', reply_markup=backbutton())
    await Commentstate.comment.set()

@dp.message_handler(state=Commentstate.comment)
async def getcomment(message: Message, state: FSMContext):
    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
        await state.finish()
    else:

        chat_id = message.chat.id
        fullname = message.from_user.full_name
        username = message.from_user.username
        user = message.from_user.get_mention()
        print(user)
        print(message.from_user)
        text = f'Ismi: {fullname}\n' \
               f'User name: @{username}\n' \
               f'Telegram id: {chat_id}\n' \
               f'User: {user}\n\n\n' \
               f'Comment: \n\n{message.text}' \

        await bot.send_message(ADMINS[0], text)
        await message.answer('Xabaringiz menejerga yetkazildi ✅.\n\nFikr va takliflaringiz uchun raxmat', reply_markup=genearatemainmenu())
        await state.finish()