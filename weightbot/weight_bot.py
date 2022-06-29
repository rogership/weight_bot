import configparser
import logging
import telebot
from manage_file import man_json


config = configparser.ConfigParser()
config.read("config.ini")
API_TOKEN = config["TelegramBot"]["token"]

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
 
@bot.message_handler(commands=["peso"])
def get_peso(message):
	try:
		response = message.text.split()
		value = float(response[1])
		date = response[2] if len(response) > 2 else ""
		bot.reply_to(message, (value, date))
		man_json(key="peso", data=value, date=date)
		bot.reply_to(message, "OK")
	except Exception as err:
		print("[Erro]", err)
		bot.reply_to(message, f"Erro {err}")

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

bot.infinity_polling()
