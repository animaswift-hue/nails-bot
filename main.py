import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Вставь сюда свой токен (в кавычках)
TOKEN = "8718735616:AAEv60UWCdxTb92u_ZUHZarnUToqXVpbXmY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Бот успешно запущен!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
