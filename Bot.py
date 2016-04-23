# -*- coding: utf-8 -*-
import telebot

API_TOKEN = '202773259:AAFhv-bdqhAyqd1CZ-j9daHIeW-HeY1QqWM'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "TAVOO")
bot.polling()