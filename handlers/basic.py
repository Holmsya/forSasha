from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards import main_kb


async def send_welcome(message: types.Message):
    await message.answer("Welcome!", reply_markup=main_kb)


async def help_answer(message: types.Message):
    await message.reply("This is my help.")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(help_answer, Text(equals="Help", ignore_case=True))