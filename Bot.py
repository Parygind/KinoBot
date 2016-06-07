# -*- coding: utf-8 -*-
import telebot
from Game import *

game=Game('http://kvester.ru/game/quest/2164?restart')
bot = telebot.TeleBot("202773259:AAFhv-bdqhAyqd1CZ-j9daHIeW-HeY1QqWM")
menu=[]
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "))))")
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.one_time_keyboard = True
    text = game.getText()
    menu = game.getMenu()
    for item in menu:
        markup.row(item)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    game.play = True

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if(game.play):
        if(game.menu.index(message.text)>=0):
            game.click(game.menu.index(message.text))
            markup = telebot.types.ReplyKeyboardMarkup()
            markup.one_time_keyboard = True
            text = game.getText()
            menu = game.getMenu()
            for item in menu:
                markup.row(item)
            bot.send_message(message.chat.id, text, reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
