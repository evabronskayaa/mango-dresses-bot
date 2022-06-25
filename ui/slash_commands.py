import types
from aiogram import Bot, Dispatcher, executor, utils, types
from db import find_id_search, find_all_stuff
from main import dp


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer(f'Hey, {message.from_user.first_name}! I am your assistant in finding the right dresses and '
                         f'jumpsuits on the MANGO website in the USA. To read more about me, you can use /help command')


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    message_text = f'Here is our functionality:\n' \
                   f'/about - our links\n' \
                   f'/list - ???\n' \
                   f'/type - ???\n' \
                   f'/search - ???\n'
    await message.answer(text=message_text)

@dp.message_handler(commands='about')
async def send_link(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com/evabronskayaa/mango-dresses-bot"),
        types.InlineKeyboardButton(text="Our Trello", url="https://trello.com/b/QM7QyoCC/пробник-бота")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Our links", reply_markup=keyboard)

@dp.message_handler(commands='list')
async def send_list(message: types.Message):
    search_models = find_id_search(message.chat.id)
    stuff = find_all_stuff()
    for st in stuff:
        st_title = st.title
        for search_model in search_models:
            search_title = search_model.title
            if st_title.find(search_title) >= 0:
                message_text = 'Строка поиска {} \r\n Найдено {}'.format(search_title, utils.markdown.hlink(st_title,
                                                                                                            st.url))
                await message.answer(text=message_text, parse_mode=ParseMode.HTML)


@dp.message_handler(commands='search')
async def send_search(message: types.Message):
    search_models = find_id_search(message.chat.id)
    for search_model in search_models:
        await message.answer(text=search_model.title)


@dp.message_handler(commands='type')
async def sent_type(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['All', 'Dresses', 'Jumpsuits']
    keyboard.add(*buttons)
    await message.answer("Well, let's choose cool looks! Tell me the type of clothes :)", reply_markup=keyboard)


# @dp.message_handler(Text(equals="All"))
# async def get_all(message: types.Message):
#     await message.reply("")
#
#
# @dp.message_handler(lambda message: message.text == "Dresses")
# async def get_dresses(message: types.Message):
#     await message.reply("")

# @dp.message_handler()
# async def echo(message: types.Message):
#     await process_search_model(message)