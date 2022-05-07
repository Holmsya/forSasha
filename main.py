from distutils.log import INFO
from json.tool import main
import logging
from aiogram import executor
from create_bot import dp
from handlers import basic

logging.basicConfig(level=logging.INFO)

basic.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)