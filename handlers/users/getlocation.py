from geopy.distance import distance

from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from data.config import latitude, longitude
from loader import dp, bot

from keyboards.default.mainmenubutoons import genearatemainmenu
from keyboards.default.otherkeyboards import generatelocationbutton
from states.location import Loaaction

@dp.message_handler(text='🗺️ Manzilimiz')
async def getlocation(message: Message ):
    await message.answer('Joylashuv o\'rningizni yuboring: ',
                         reply_markup=generatelocationbutton())

    await Loaaction.user_location.set()

@dp.message_handler(state=Loaaction.user_location)
@dp.message_handler(content_types='location', state=Loaaction.user_location)
async def sendlocation(message: Message, state: FSMContext):

    if message.text == '⬅️ Orqaga' or message.text == '/start' or message.text == '/help':
        await state.finish()
        await message.answer('Bosh menu', reply_markup=genearatemainmenu())
    elif message.location:

        userlatitude = message.location.latitude
        userlongitude = message.location.longitude
        distance_km = distance((latitude, longitude), (userlatitude, userlongitude)).km
        distance_km = round(distance_km, 2)
        await message.answer(f'Siz turgan joydan o\'quv markazigacha {distance_km} km', reply_markup=genearatemainmenu())
        await message.answer_location(latitude=latitude, longitude=longitude)
        await state.finish()
    else:
        await message.answer('Joylashuv yuborish uchun pastdagi tugmani bosing')
