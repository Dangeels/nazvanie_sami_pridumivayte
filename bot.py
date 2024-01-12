import config
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton, MenuButtonDefault
import json
import text
print('хуй')

bot = telebot.TeleBot(config.bot_token)

@bot.message_handler(commands=['start','help','referral'])
def start(m):
    c1 = types.BotCommand(command='myprofile', description='Start the Bot')
    c2 = types.BotCommand(command='help', description='Click for Help')
    c3 = types.BotCommand(command='referral', description='Something')
    bot.set_my_commands([c1, c2, c3])
    bot.set_chat_menu_button(m.chat.id, types.MenuButtonCommands('commands'))


    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    next_btn = KeyboardButton('все понятно! пройти регистрацию')
    markup.add(next_btn)

    x = telebot.util.extract_command(m.text)

    bot.send_message(m.chat.id,text=text.text[x],reply_markup=markup)
    bot.send_message(m.chat.id,text.text['1']) if x == 'start' else None

questions = []


@bot.message_handler(commands=['myprofile'])
def profile(m):
    ...




bot.infinity_polling()