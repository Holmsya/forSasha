from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

help_button = KeyboardButton("Help")
button1 = KeyboardButton("Button1")

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)

main_kb.add(help_button)
# main_kb.add(help_button).add(button1)
# main_kb.add(help_button).insert(button1)
# main_kb.row(help_button, button1)