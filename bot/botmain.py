# bot - @Shashlik5Bot
from aiogram import Bot, Dispatcher, executor, types
import bot.config  # create in bot a file config.py with constant TOKEN = "*your token*"  !gitignore

TOKEN = bot.config.TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["help", "start"])
async def commands(message: types.Message):
    comm = message.get_command()
    if comm == "/help":
        await message.answer("Укажите населенный пункт, в котором вы сейчас.\nНапример:")
        await message.answer("Екатеринбург")
        await message.answer("Сысерть. 2 градуса. Солнечно")
        await message.answer(
            "После получения информации вы можете запросить топ-список мест через /top")
        await message.answer("/top")
        await message.answer("Сысерть. 2 градуса. Солнечно\nБерезовский. -1 градус. Снег")
    elif comm == "/start":
        await message.answer(
            "Здравствуйте! Я бот, который покажет вам лучшие места рядом в вами. Укажите своё местоположение (Например 'Екатеринбург')")
    elif comm == "/top":
        # тут должен быть запрос на сервер обработка ответа
        # await message.answer()
        ...


@dp.message_handler()
async def getPosition(message: types.Message):
    # тут должен быть запрос на сервер обработка ответа
    # await message.answer()
    ...

def startBot():
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
