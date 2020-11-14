from aiogram import Bot, Dispatcher, executor, types
import bot.config  #create in bot file config.py with constant TOKEN = "*your token*"

TOKEN = bot.config.TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def startBot():
    executor.start_polling(dp, skip_updates=True)