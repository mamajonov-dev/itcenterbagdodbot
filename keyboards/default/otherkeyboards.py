from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup


def generatelocationbutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(

        KeyboardButton(text='Joylashuv o\'rini yuborish',
                       request_location=True)

    )
    markup.add(
        KeyboardButton(text='⬅️ Orqaga')
    )
    return markup


def generateconfirmbutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(

        KeyboardButton(text='Ha'),
        KeyboardButton(text="Yo'q")

    )
    return markup
