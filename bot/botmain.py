# bot - @Shashlik5Bot
import requests
from aiogram import Bot, Dispatcher, executor, types

import bot.config  # create in bot a file config.py with constant TOKEN = "*your token*"  !gitignore
import config

ServerURL = f"http://{config.host}:{config.port}/weatherHandler"
TOKEN = bot.config.TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["help", "start"])
async def commands(message: types.Message):
    comm = message.get_command()
    if comm == "/help":
        await message.answer(
            "Specify the settlement in which you are now and the search radius. For instance:")
        await message.answer("Yekaterinburg 50")
        await message.answer("Sysert. °2 С. Sunny\nBerezovsky. -1 °С. Snow")
    elif comm == "/start":
        await message.answer(
            "Hello! I am a bot that will show you the best places near you. Indicate your location (For example: Yekaterinburg 20)")


@dp.message_handler()
async def getPosition(message: types.Message):
    try:
        city, radius = message.text.split()
        fromserver = requests.post(ServerURL, data={'city': city, 'radius': radius})
        if fromserver.text[0] == '{' and fromserver.text[-2] == '}':
            dictFromServer = eval(fromserver.text)
            cities = dictFromServer['city']
            temps = dictFromServer['temp']
            weathers = dictFromServer['weather']
            answerStr = '\n'.join(
                [f"{cities[i]}. {temps[i]} °C. {weathers[i]}" for i in range(len(cities))])
            await message.answer(answerStr)
    except:
        await message.answer("Incorrect input")



def startBot():
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
