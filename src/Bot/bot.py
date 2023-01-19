import telebot
from .config import settings
from datetime import datetime
from .Messages.messages import Message

TOKEN=settings.SECRET_KEY


class Bot:

	bot = telebot.TeleBot(TOKEN)	

	@bot.message_handler(commands=['start'])
	def send_welcome(message):
		bot.reply_to(message, "Howdy, how are you doing?")

	@bot.message_handler(commands=['HOJE'])
	def get_currently_meal(message):
		bot.reply_to(message, "Howdy, how are you doing?")

	@bot.message_handler(func=lambda T: True)
	def generic_handler(user_message):
		message = Message(user_message)
		if message.is_valid():
			print(f'[{user_message.from_user.username} | {user_message.from_user.first_name} - {datetime.now()}]')
			message.verify_message()
			bot.reply_to(user_message, message.menu())
		else:
			bot.reply_to(user_message, "Opáá, não entendi isso não")

		


bot = Bot().bot






