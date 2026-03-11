import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8718735616:AAEv60UWCdxTb92u_ZUHZarnUToqXVpbXmY"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки Inline (они нажимаются)
def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Онлайн запись 📆", callback_data="book")],
        [InlineKeyboardButton(text="Прайс-лист 💵", callback_data="price")],
        [InlineKeyboardButton(text="Фото работ 📸", callback_data="gallery")],
        [InlineKeyboardButton(text="Правила 📋", callback_data="rules")],
        [InlineKeyboardButton(text="По вопросам 💬", callback_data="contact")]
    ])

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Выберите раздел:", reply_markup=get_main_menu())

# Логика нажатий
@dp.callback_query(F.data == "book")
async def book(call: types.CallbackQuery):
    await call.message.answer("Ссылка на онлайн запись: [ССЫЛКА]")

@dp.callback_query(F.data == "price")
async def price(call: types.CallbackQuery):
    await call.message.answer("Наш прайс-лист: [ТЕКСТ ИЛИ ФОТО]")

# ... и так далее для каждого callback_data ...

# --- Заглушка для Render ---
async def handle(request): return web.Response(text="OK")
async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app); await runner.setup()
    await web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080))).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
