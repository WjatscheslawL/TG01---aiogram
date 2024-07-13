import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
import requests
from config import TOKEN, API_BITCOIN, API_WETTER


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/bitcoin\n/photo\n/wetter")


@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')


@dp.message(F.photo)
async def react_photo(message: Message):
    lists = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(lists)
    await message.answer(rand_answ)


@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://c.ekstatic.net/shared/images/destination/v1/airports/DXB/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/KUL/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/BKK/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/SIN/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/HKG/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/HAN/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/IKA/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/DEL/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/KHI/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/LHE/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/PEK/600x360.jpg',
'https://c.ekstatic.net/shared/images/destination/v1/airports/MCT/600x360.jpg']
    photos = random.choice(list)
    random_photo = random.choice(photos)
    await message.answer_photo(photo=photos, caption='Это супер крутая картинка')


@dp.message(Command('bitcoin'))
async def send_bitcoin_price(message: Message):
    try:
        response = requests.get(API_BITCOIN)
        data = response.json()
        price = data['bitcoin']['usd']
        # await message.answer('Der aktuelle Bitcoin-Preis wird abgefragt')

        await message.answer(f"Der aktuelle Bitcoin-Preis beträgt ${price:.2f}")
    except Exception as e:
        await message.answer(f"Entschuldigung, es gab einen Fehler beim Abrufen der Bitcoin-Daten: {e}")


@dp.message(Command('wetter'))
async def wetter(message: Message):
    # адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
    city = 'Tomsk'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_WETTER}&units=metric"
    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    # прописываем формат возврата результата
    noroda = response.json().get('main', [])
    #await message.answer(str(noroda.get('temp')))
    await message.answer(f"Der aktuelle Lufttemperatur in {city} : {noroda.get('temp'):.2f} C°")


def get_weather(city):

    # адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    # прописываем формат возврата результата
    return response.json()

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
