from aiogram.types import Message
from loader import dp


@dp.message_handler(text='🟢 Biz haqimizda')
async def aboutus(message: Message):
    text = f"IT Center Bag'dod \n Bagdad IT Academy\n" \
           f"\nIT Park Uzbekistan filiali hisoblanib, 2020-yil dekabr oyida ochilgan. 4 yildan ortiq faoliyatga ega. Shu yil davomida 900 dan ortiq o'quvchilarga malakali mentorlar bilim berishgan. Real loyihalar bilan ishlashgan\n\n" \
           f"Manager: Mamajonov Nurmuhammad\n\n" \
           f"☎️ +998917871199 \n" \
           f"☎️ 998998871199\n" \
           f"@NurmuhammadMamajonov \n\n" \
           f"📍Hududi: Farg'ona viloyati, Bag'dod tumani\n" \
           f"🗺️Manzil:  Tuman pochta binosi 2-qavati\n" \
           f"Mo'ljal: Tuman hokiniyati binosi yon tarafida\n\n" \
           f"Telegram kanal: @bagdaditacademy\n" \
           f"Instagram:\n https://www.instagram.com/invites/contact/?i=1l22pirnilofd&utm_content=romi5gy"
    await message.answer(text)
