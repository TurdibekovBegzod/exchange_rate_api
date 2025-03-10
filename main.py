from aiogram import Bot, Dispatcher
import functions
from asyncio import run


dp = Dispatcher()
bot = Bot(token = "Your bot token")
#===================================
async def startup(bot : Bot):
    await bot.send_message(chat_id = "Your tg id.", text = "Bot ishga tushdi! ✅")

from collections import deque

async def shutdown(bot : Bot):
    await bot.send_message(chat_id = "your tg id", text = "Bot ishdan to'xtadi! ❌")

#=================================================
async def main():
    dp.startup.register(startup)

    dp.message.register(functions.answer)

    dp.shutdown.register(shutdown)
    await dp.start_polling(bot)

run(main())
