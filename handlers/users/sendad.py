# from aiogram.types import Message
# import sqlite3
# from aiogram.dispatcher import FSMContext
# from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
# from dotenv import load_dotenv
# load_dotenv()
# import os
#
# from keyboards.default.mainmenubutoons import backbutton, genearatemainmenu
# from keyboards.default.otherkeyboards import generateconfirmbutton
# from loader import dp, bot
# from states.sendadstates import SendadState
#
# admin = os.getenv('ADMINS')
#
# @dp.message_handler(commands='sendad')
# async def senad(message: Message):
#     if str(message.chat.id) in admin:
#         await message.answer('Reklamani yozing: ', reply_markup=backbutton())
#         await SendadState.ad.set()
#     else:
#         pass
#
# @dp.message_handler(state=SendadState.ad)
# async def getad(message: Message, state: FSMContext):
#     text = message.text
#     if text == '⬅️ Orqaga':
#         await message.answer('Bosh menu', reply_markup=genearatemainmenu())
#         await state.finish()
#     else:
#         await state.update_data({'ad': text})
#         await message.answer('Tasdiqlash: Jo\'natilsinmi?', reply_markup=generateconfirmbutton())
#         await SendadState.resquest.set()
#
#
# @dp.message_handler(state=SendadState.resquest)
# async def getimage(mesasge: Message, state: FSMContext):
#     if mesasge.text == 'Ha':
#         data = await state.get_data()
#         text = data['ad']
#         database = sqlite3.connect('././database.sqlite')
#         cursor = database.cursor()
#         cursor.execute('''SELECT telegram_id FROM users''')
#         users = cursor.fetchall()
#         for user in users:
#             chat_id = user[0]
#             await bot.send_message(chat_id, text, reply_markup=genearatemainmenu())
#         await state.finish()
#     elif mesasge.text == "Yo'q" or mesasge.text == '/start':
#         await mesasge.answer('Bekor qilindi', reply_markup=genearatemainmenu())
#         await state.finish()
#     else:
#         await mesasge.answer('Variantlardan birini tanlang')
#
#
