from aiogram import Dispatcher, Bot

import asyncio
from bot.bot import router

bot = Bot(token="7830706902:AAFwKOsgRHVQfUN4jPxLvZI0mu6LypAjUCc")

async def main():
    
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())