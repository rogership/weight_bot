import telebot

API_TOKEN = "5401394631:AAHD_3QN9YDt56bgPhq9mnNU-OOdy3oE5aY"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

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

bot.infinity_polling()