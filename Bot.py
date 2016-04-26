# -*- coding: utf-8 -*-
import telebot
from flask import Flask, request

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "TAVOO")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@app.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_messages([telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://damp-scrubland-49674.herokuapp.com/Bot")
    return "!", 200

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)