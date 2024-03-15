from aiogram.types import Message
import sqlite3
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.cousesbuttons import generatecoursebuttons
from keyboards.default.mainmenubutoons import genearatemainmenu
from states.getcourse import Getcourse


@dp.message_handler(text='💻 Kurslar')
async def getcourses(message: Message, state: FSMContext):
    await message.answer('Kurlarimiz: ', reply_markup=generatecoursebuttons())
    await Getcourse.name.set()


@dp.message_handler(state=Getcourse.name)
async def getcourse(message: Message, state: FSMContext):
    text = message.text

    if text == '⬅️ Orqaga' or text == '/start':
        await message.answer('Asosiy menu', reply_markup=genearatemainmenu())
        await state.finish()
    elif text == '💻 Front end':
        await message.answer(f'Kurs nomi: Front end \n\n\n'
                             f'Front-End nima ?\n\n'
                             f'Front-End dasturlovchi veb-saytning foydalanuvchiga ko’rinadigan qismini'
                             f' tayyorlash bilan shug’ullanadi. Masalan siz veb-saytlarda ko’radigan oddiygina '
                             f'tugma uchun ham Front-End dasturlovchi mehnat qilib kod yozadi. Ya’ni siz brauzer'
                             f' orqali ekranda ko’rib turadigan barcha narsani tayyorlash Front-End dasturchining '
                             f'vazifasi va mana shu tayyorlangan ishlarning jamlanmasi veb-saytning Front-End qismi'
                             f' deyiladi. Yanada soddaroq tushuntiradigan bo’lsam siz veb-sayt nomini brauzerga '
                             f'yozib, veb-saytga kirganingizda sizga ko’rinib turgan qismi Front-End qismi hisoblanadi.\n\n'
                             f'Kurs narxi: 300 000 so\'m\n'
                             f'Birinchi oy uchun chegirmadagi narx: 150 000 so\'m\n'
                             f'Kurs davomiyligi: 8 oy')
    elif text == '💻 Backend':
        await message.answer(f"Kurs nomi: Backend\n\n"
                             f"Backend dasturlash asosan saytning yoki mobile ilovalarni qanday ishlashini, server qismi, maʼlumotlar bazasi va brauzer oʻrtasida aloqani taʼminlaydi."
                             f"\n\nXo'sh, bu kasb egalarining vazifalari nimalardan iborat?\n\n"
                             f"▫️ Backend dasturchilar veb-sahifalar va ilovalarni bosilganda tez yuklanishini nazorat qiladi;\n\n"
                             f"▫️ Backend dasturchilar shuningdek saytga obuna bo'lganlarni ma'lumotlar bazasiga qayd etib borilishi uchun ham javobgar hisoblanadi;\n\n"
                             f"▫️ Veb-sayt yoki ilovada sodir bo'ladigan har qanday faoliyatni aniqlash va uni tezda hal qilish;\n\n"
                             f"▫️ Shuningdek, foydalanuvchi tomonidan taqdim etilgan barcha ma'lumotlarni to'plashlari va bir xillikda birlashtirishlari kerak. Bu asosan ma'lumotlar bazasiga tegishli.\n\n\n"
                             f"Kurs narxi: 400 000 so'm\n"
                             f"Birinchi oy uchun chegirmadagi narx: 200 000 so'm\n"
                             f"Kurs davomiyligi: 8 oy")
    elif text == '💻 Komyuter savodxonligi':
        await message.answer(f"Kurs nomi: Kompyuter savodxonligi\n\n"
                             f"Kompyuter savodxonligi - bu: \n"
                             f"kerakli parametrlarga muvofiq kompyuterni tanlashni bilish;\n"
                             f"periferik qurilmalarni bilish va ularni ulay olish;\n"
                             f"kamida Windows operatsion tizimini bilish;\n"
                             f"Office'ning asosiy dasturlari - Word, Excel, PowerPoint'ni bilish;\n"
                             f"yangi ilovalarni yuklash va o'zlashtirishni bilish;\n"
                             f"Internetda ishlashni va brauzerlarni bilish;\n"
                             f"axborot qidirish ko'nikmalariga ega bo'lish.\n\n"
                             f"Siz tajribali kompyuter foydalanuvchisi bo'lishni istaysizmi? Unda IT Markaz kurslariga yoziling\n\n"
                             f"Kurs narxi: 150 000 so'm\n"
                             f"Kurs davomiyligi: 1 oy")
    elif text == '💻 Python':
        await message.answer(f"Kurs nomi: Python dasturlash\n\n"
                             f"Python da veb-ilovava neyro-tarmoqlar yaratiladi, ilmiy hisob-kitoblar amalga oshiriladi va jarayonlar avtomatlashtiriladi. Siz talab etilgan dasturlash tilida noldan boshlab dasturlashni organib olasiz, sayyohlik agentligi uchun Telegram-botlar yaratasiz va oz karyerangizni boshlashingiz uchun eng qulay va onson yo’l."
                             f"\n\nKurs narxi: 400 000 so'm\n"
                             f"Birinchi oy uchun chegirmadagi narx: 200 000 so'm\n"
                             f"Kurs davomiyligi: 3 oy")
    elif text == '💻 Mukammal telegram bot':
        await message.answer(f"Kurs nomi: Mukammal telegram bot\n\n"
                             f"Bugungi kunda korxonalarning yaratayotgan xizmat turlarining deyarli barchasi telegram orqali faoliyatni tashkil etgan. Foydalanuvchilarning asosiy trafigi aynan shu tarmoqqa tegishli ekanligi ham hech kimga sir emas. Bu kabi xizmat turlarini ishlab chiqish esa, o'z navbatida, yuqori darajali jarayonlarni bosib o'tadi.\n"
                             f"Keling, dastlab bot tushunchasiga to'xtalib o'taylik. Telegram bot - shu tarmoqda ishlaydigan kichik bir dasturcha. U ma'lum bir tizimni boshqaradi. Ular orqali, kanallarni, guruhlarni nazorat qilish yoxud mavjud loyihalarni tanishtirish, shu bilan birgalikda, xizmat turlarini yo'lga qo'yish ancha oson kechadi."
                             f"\n\nKurs narxi: 400 000 so'm\n"
                             f"Birinchi oy uchun chegirmadagi narx: 200 000 so'm\n"
                             f"Kurs davomiyligi: 3 oy")
    elif text =='💻 Grafik dizayn':
        await message.answer(f"Kurs nomi: Grafik dizayn\n\n"
                             f"Har qanday biznesning o‘z uslubi, timsoli, shakli bo‘ladi. Dunyoda bizneslar, kompaniyalar, firmalar, mahsulotlar bor ekan, reklama sohasi o‘lmaydi. Reklama sohasining markazida esa – aynan grafik dizayner turadi.\n\n"
                             f"Bizning “Grafik dizayn” o‘quv kursimizda taʼlim olib, siz eng mashhur Adobe Photoshop, Abobe Illustrator va CorelDRAW dasturlarini puxta egallaysiz va mehnat bozorida yuqori talabga ega soha vakiliga aylanasiz!"
                             f"\n\nKurs narxi: 300 000 so'm\n"
                             f"Birinchi oy uchun chegirmadagi narx: 150000 so'm\n"
                             f"Kurs davomiyligi: 6 oy")
    elif text =='💻 Autocad (uylarni loyihalash)':
        await message.answer(f"""Kurs nomi:  Autocad (uylarni loyihalash)
        
        AUTOCAD TIZIMDA LOYIHALASH VA MUHANDISLIK
 
        AutoCAD grafik ilovasi yordamida tezda ko'nikmalarga ega bo'lishni xohlaysizmi? AutoCAD kursi uning noyob xususiyatlaridan foydalanishni o'rganishi kerak bo'lgan har bir kishi uchun mo'ljallangan. Sinflar o'quvchilar o'quv jarayonida amaliy qatnashish, AutoCAD tamoyillarini tez va etarli darajada o'zlashtirish imkoniyatiga ega bo'ladigan tarzda yaratilgan.
        AutoCAD kursining o'quv dasturi dizayn va muhandislik hujjatlarini ishlab chiqish jarayonini avtomatlashtirish imkoniyatlarini o'zlashtirishga qaratilgan. AutoCAD tizimining asosiy maqsadi turli xil mavzudagi loyihalar uchun chizmalar yaratishdir. Bu ob'ektlar, turli mexanizmlarning loyihalari, shuningdek, elektr sxemalarini ishlab chiqish bo'lishi mumkin.                    
        Kurs oxirida talabalar sertifikat oladilar.
        To'lovning har qanday shakli.
                             
        Kurs narxi: 400 000 so'm
        Kurs davomiyligi: 3 oy""")
