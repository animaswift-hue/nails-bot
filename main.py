import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Твой токен (я вижу, ты его уже вставил, это отлично!)
TOKEN = "8718735616:AAEv60UWCdxTb92u..." 

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция главного меню
def get_main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Онлайн запись 📆", callback_data="online_book")],
        [InlineKeyboardButton(text="Прайс-лист 💵", callback_data="price")],
        [InlineKeyboardButton(text="Наши работы 📸", callback_data="gallery")],
        [InlineKeyboardButton(text="Правила 📋", callback_data="rules")],
        [InlineKeyboardButton(text="По вопросам 💬", callback_data="contact")]
    ])
    return keyboard

# Кнопка возврата
def get_back_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="« Вернуться", callback_data="main_menu")]
    ])

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Добро пожаловать в студию! ✨\nВыберите нужный раздел:", reply_markup=get_main_menu())

@dp.callback_query(F.data == "main_menu")
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Главное меню:", reply_markup=get_main_menu())

# --- Обработка кнопок ---

@dp.callback_query(F.data == "price")
async def show_price(callback: types.CallbackQuery):
    await callback.message.edit_text("Вот наш прайс-лист (здесь будет фото):", reply_markup=get_back_button())

@dp.callback_query(F.data == "rules")
async def show_rules(callback: types.CallbackQuery):
    await callback.message.edit_text("📋 Наши правила:\n1. Запись по предоплате.\n2. Отмена за 24 часа.", reply_markup=get_back_button())

@dp.callback_query(F.data == "contact")
async def show_contact(callback: types.CallbackQuery):
    await callback.message.edit_text("По всем вопросам пишите: @тег_девушки", reply_markup=get_back_button())

@dp.callback_query(F.data == "online_book")
async def online_book(callback: types.CallbackQuery):
    await callback.message.edit_text("Для записи напишите нам в ЛС или перейдите по ссылке:", reply_markup=get_back_button())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
