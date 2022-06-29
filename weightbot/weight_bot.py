##Script that receives messages from bot belonged group API or
#directly from bot.

import logging
import telebot
from data_json import man_json

API_TOKEN = "5401394631:AAHD_3QN9YDt56bgPhq9mnNU-OOdy3oE5aY"

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
    
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)
##
# @bot.channel_post_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.channel_post_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

bot.infinity_polling()
