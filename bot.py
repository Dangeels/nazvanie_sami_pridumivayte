import config
import telebot
from dataclasses import dataclass
from telebot import types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton, MenuButtonDefault
import json
import text


bot = telebot.TeleBot(config.bot_token)

@bot.message_handler(commands=['start','help','referral'])
def start(m):
    c1 = types.BotCommand(command='myprofile', description='Start the Bot')
    c2 = types.BotCommand(command='help', description='Click for Help')
    c3 = types.BotCommand(command='referral', description='Something')
    bot.set_my_commands([c1, c2, c3])
    bot.set_chat_menu_button(m.chat.id, types.MenuButtonCommands('commands'))


    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    next_btn = KeyboardButton('инструкция')
    markup.add(next_btn)

    x = telebot.util.extract_command(m.text)

    bot.send_message(m.chat.id,text=text.text[x],reply_markup=markup)
    bot.send_message(m.chat.id,text.text['1']) if x == 'start' else None

@dataclass
class Questions:
    question: str

questions = [
    Questions('Сколько тебе лет?'),
    Questions('Как тебя зовут(Имя Фамилия)?'),
    Questions('В каком ты классе?'),         # Номер класса в сообщении, буква в кнопках
    Questions('Отправь свою фотку')
             ]

@bot.message_handler(regexp='инструкция')
def instruction(m):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Подарки и бонусы')
    markup.add(btn)

    bot.send_message(m.chat.id,text.text['help'], reply_markup=markup)
    bot.send_message(m.chat.id, text.text['ne_ebu'])
@bot.message_handler(regexp='Подарки и бонусы')
def ref(m):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Пройти регистрацию')
    markup.add(btn)

    bot.send_message(m.chat.id, text.text['referral'],reply_markup=markup)

@bot.message_handler(regexp='Пройти регистрацию')
def registration(m):
    bot.send_message(m.chat.id, text.text['important'])
    bot.send_message(m.chat.id, text.text['anketa'])


@bot.message_handler(commands=['myprofile'])
def profile(m):
    ...

def p(s:None=None) -> None:
    print('')

def p(s:None=None) -> None:
    pass

def p(s:None=None) -> None:
    pass

print('')
bot.infinity_polling()
