# -*- coding: utf-8 -*-
import telebot

API_TOKEN = '202773259:AAFhv-bdqhAyqd1CZ-j9daHIeW-HeY1QqWM'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'TAVO')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
bot.polling()