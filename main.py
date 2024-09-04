import telebot
import requests

Token = "7512423699:AAGId_s4clww1dMSCvHcYbPhj_RPVYs-Y2A"
bot = telebot.TeleBot(Token)
URL = "https://api.binance.com/api/v1/ticker/price/symbol=btcusdt"

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hey, how are you doing?")

@bot.message_handler(func=lambda message:True)
def echo_message(message):
	if message.text == "help" or message.text == "Help":
		bot.reply_to(message, "What can I do for you?")

	elif message.text == "Hi" or message.text == "hi" or message.text == "سلام" or message.text == "Hello" or message.text == "hello":
		bot.reply_to(message, "Hello love, this is Melika")
	# elif message.text != "":
	# 	bot.reply_to(message, "Something's wrong...!")
	# 	bot.reply_to(message, message.text)

	else:
		symbol = message.text.upper()
		response = requests.get(f"https://api.binance.com/api/v1/ticker/price?symbol={symbol}")
		print(response.status_code)
		if response.status_code == 200:
			data = response.json()
			print(data)
			bot.reply_to(message, f"{data['symbol']} price is {data['price']}")
		else:
			bot.reply_to(message, "your symbol is not true!!")

bot.infinity_polling()