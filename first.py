#!/usr/bin/python
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram
import threading

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
def echo(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
def key_t(bot, update):
	custom_keyboard = [['/start', 'top-right'], ['bottom-left', 'bottom-right']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)



def shutdown():
	updater.stop()
	updater.is_idle = False

def upload(bot, update):
	bot.send_message(chat_id=update.message.chat_id, )


def stop(bot, update):
#	updater.idle()
#	updater.stop()
	#updater.is_idle = False
	#exit()
	threading.Thread(target=shutdown).start()


updater = Updater(token='224391427:AAEc0CvVN4SM_FZ0vi0anlCEuKptRysQSa0')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

board_handler = CommandHandler('key_t', key_t)
dispatcher.add_handler(board_handler)


stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)



updater.start_polling()
exit()
