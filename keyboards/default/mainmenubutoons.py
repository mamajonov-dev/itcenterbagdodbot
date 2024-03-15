from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

def genearatemainmenu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='🎁 Musobaqaga (hacatonga) ro\'yxatdan o\'tish')
    )
    markup.add(
        KeyboardButton(text='🟢 Biz haqimizda'),
        KeyboardButton(text='💻 Kurslar'),
    )
    markup.add(
        KeyboardButton(text='📝 Kurslarga ro\'yxatdan o\'tish')
    )
    markup.add(
        KeyboardButton(text='🗺️ Manzilimiz'),
        KeyboardButton(text='📝 Fikr va takliflar')
    )
    return markup

def backbutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='⬅️ Orqaga'),

    )

    return markup
