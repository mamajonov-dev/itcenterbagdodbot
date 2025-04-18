from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


def generatecoursebuttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='💻 IT Kids'),
        KeyboardButton(text='💻 ENGLISH for Kids'),
    )
    markup.add(
        KeyboardButton(text='💻 Front end'),
        KeyboardButton(text='💻 Backend')
    )
    markup.add(
        KeyboardButton(text='💻 Komyuter savodxonligi'),
        KeyboardButton(text='💻 Mukammal telegram bot')
    )
    markup.add(
        KeyboardButton(text='💻 Grafik dizayn'),
        KeyboardButton(text='💻 Python')
    )
    markup.add(
        KeyboardButton(text='💻 Autocad (uylarni loyihalash)'),
    )
    markup.add(KeyboardButton(text='⬅️ Orqaga'))

    return markup
