from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

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


def channelbuuton():
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(
        InlineKeyboardButton(url='https://t.me/bagdaditacademy', text='Bagdad IT Accademy'),
    )
    return markup



def hacatontest():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='0'),
        KeyboardButton(text="30"),
        KeyboardButton(text="3"),
        KeyboardButton(text="27"),
        KeyboardButton(text="Xatolik"),
        KeyboardButton(text="10"),
    )
    return markup