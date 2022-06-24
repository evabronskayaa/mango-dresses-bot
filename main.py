import logging
import asyncio
import requests
from bs4 import BeautifulSoup as b

from aiogram import Bot, Dispatcher, executor, utils, types
from aiogram.types import ParseMode

from db import process_search_model, init_db, find_id_search, find_all_cards
from config import URL, TOKEN

# r = requests.get(URL)
# print(r.status_code)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='list')
async def send_list(message: types.Message):
    pass


@dp.message_handler(commands='search')
async def send_search(message: types.Message):
    pass


@dp.message_handler()
async def echo(message: types.Message):
    await process_search_model(message)


async def scheduled(wait_for, parser):
    while True:
        await asyncio.sleep(wait_for)
        # await parser.parse()

if __name__ == '__main__':
    init_db()
    # parser = ParseVideoCard(url=URL, bot=bot)
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10, None))
    executor.start_polling(dp, skip_updates=True)
