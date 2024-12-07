import asyncio
from aiogram import F, Router,types
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters.command import CommandStart
from .keyboard import push_keyboard


router = Router()
file_ids = []


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Привет,я Вован,кроме любви к маленьким мальчикам я так-же очень сильно люблю историю,давай и тебя научим ее любить")
    # await message.answer("Когда дрочил Пётр Первый?",reply_markup=push_keyboard("Вчера","Мне на лицо","Сегодня","Завтра")):
    image_from_url = URLInputFile("https://icdn.lenta.ru/images/2024/07/05/15/20240705154034793/detail_f30b958fd145c79b5dea374c223ad6e2.jpg")
    await message.answer_photo(image_from_url,caption="Когда дрочил Пётр Первый?",reply_markup=push_keyboard("Вчера","Мне на лицо","Сегодня","Завтра"))

@router.callback_query(F.data == "2") 
async def process_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer("\"Да,я вчера дрочил\"-Пётр Первый,вчера")
    

