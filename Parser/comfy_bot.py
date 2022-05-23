from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from next_parser import collect_data
from aiofiles import os


bot = Bot(token='5150680660:AAFLeXO2e2n6cz8QPGF1wEhmyc5Q7D7lm6I')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Kyiv', 'Lviv'] # Обьеденим несколько кнопок в список (названия городов)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) # Создаём объект клавиатуры
    keyboard.add(*start_buttons) # Добавляем в клавиатуру с помощью метода add наш список кнопок

    await message.answer('Please select a City', reply_markup=keyboard)

@dp.message_handler(Text(equals='Kyiv'))
async def kyiv_city(message: types.Message):
    await message.answer('Please waiting...')
    chat_id = message.chat.id
    await send_data(city_code='506', chat_id=chat_id)

@dp.message_handler(Text(equals='Lviv'))
async def lviv_city(message: types.Message):
    await message.answer('Please waiting...')
    chat_id = message.chat.id
    await send_data(city_code='2050', chat_id=chat_id)


async def send_data(city_code='506', chat_id=''):
    file = await collect_data(city_code=city_code)
    await bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
    await os.remove(file)

if __name__ == '__main__':
    executor.start_polling(dp)