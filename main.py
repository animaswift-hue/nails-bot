import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8718735616:AAEv60UWCdxTb92u_ZUHZarnUToqXVpbXmY"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КНОПКИ ---
def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Онлайн запись 📆", callback_data="book")],
        [InlineKeyboardButton(text="Прайс-лист 💵", callback_data="price")],
        [InlineKeyboardButton(text="Наши работы 📸", callback_data="gallery")],
        [InlineKeyboardButton(text="Правила 📋", callback_data="rules")],
        [InlineKeyboardButton(text="По вопросам 💬", callback_data="contact")]
    ])

# --- ЛОГИКА ---
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Добро пожаловать в Nails Bot! ✨", reply_markup=get_main_menu())

@dp.callback_query(F.data == "book")
async def book(call: types.CallbackQuery):
    await call.message.edit_text("Для записи напишите: @тег_девушки", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="« Назад", callback_data="menu")]]))

@dp.callback_query(F.data == "price")
async def price(call: types.CallbackQuery):
    await call.message.edit_text("Наш прайс-лист: ...", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="« Назад", callback_data="menu")]]))

@dp.callback_query(F.data == "menu")
async def back_to_menu(call: types.CallbackQuery):
    await call.message.edit_text("Выберите раздел:", reply_markup=get_main_menu())

# --- ВЕБ-СЕРВЕР (чтобы Render не выключал бота) ---
async def handle(request): return web.Response(text="Бот в сети!")
async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app); await runner.setup()
    await web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080))).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
