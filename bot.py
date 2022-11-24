import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia as wk
wk.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token='#')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(messages:types.Message):
    ism = messages.from_user.full_name
    await messages.answer(f"Assalomu alaykum {ism}.\n Qidirmoqchi bo`lgan ma`lumotingizni kiriting!")

@dp.message_handler(commands=['admin'])
async def admin(messages:types.Message):
    admin = "@Ramziddin_17_17"
    await messages.answer(f"Bot admini {admin}")

@dp.message_handler(commands=['help'])
async def help(messages:types.Message):
    await messages.answer("Bu botimiz orqali siz faqatgina wikipediada mavjud ma`lumotlarni olishingiz mumkin va bu faqat "
                          "o`zbek tiliga oid ma`lumotlarni chiqarib beradi")

@dp.message_handler()
async def start(message:types.Message):
    try:
        soz = wk.summary(message.text)
        await message.answer(soz)
    except:
        await message.answer("Bunday wikipedia mavjud emas")

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)

