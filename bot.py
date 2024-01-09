import config
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton, MenuButtonDefault

bot = telebot.TeleBot(config.bot_token)





@bot.message_handler(commands=['start'])
def start(m):
    c1 = types.BotCommand(command='start', description='Start the Bot')
    c2 = types.BotCommand(command='help', description='Click for Help')
    c3 = types.BotCommand(command='go', description='Something')
    bot.set_my_commands([c1, c2, c3])
    bot.set_chat_menu_button(m.chat.id, types.MenuButtonCommands('commands'))


    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    next_btn = KeyboardButton('все понятно! пройти регистрацию')
    markup.add(next_btn)

    text = f'Привет {m.from_user.first_name}!'
    bot.send_message(m.chat.id, text)
    bot.send_message(m.chat.id,text='fuck',reply_markup=markup)


class Anketa:
    

@bot.message_handler(regexp='все понятно! пройти регистрацию')
def profile(m):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    next_btn = KeyboardButton('net')
    markup.add(next_btn)

    bot.send_message(m.chat.id,text='123',reply_markup=markup)

bot.infinity_polling()