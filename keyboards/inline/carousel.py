from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

product_cb = CallbackData('product', 'id', 'action')


def product_markup(idx, selected_stuff):
    global product_cb

    markup = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton('⬅️', callback_data=product_cb.new(id=idx, action='decrease'))
    next_btn = InlineKeyboardButton('➡️', callback_data=product_cb.new(id=idx, action='increase'))
    markup.row(back_btn, next_btn)
    return markup