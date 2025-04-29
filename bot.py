from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

# Получаем токен из переменной окружения
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(
        text="Podval Community", 
        url="https://t.me/podvalnw"
    )
    keyboard.add(button)

    welcome_text = (
        "Welcome to Podval Network Bot 🛍️\n\n"
        "Your simple and convenient P2P marketplace for buying and selling digital assets."
    )

    await message.answer(welcome_text, reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
