import cherrypy
import telebot
import logging


API_TOKEN = '202773259:AAFhv-bdqhAyqd1CZ-j9daHIeW-HeY1QqWM'

WEBHOOK_HOST = "https://damp-scrubland-49674.herokuapp.com/Main"
WEBHOOK_PORT = int(os.environ.get('PORT', '8443'))  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
           'content-type' in cherrypy.request.headers and \
           cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_messages([update.message])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

bot.remove_webhook()

bot.set_webhook(url="https://damp-scrubland-49674.herokuapp.com/Main")

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
})

cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})