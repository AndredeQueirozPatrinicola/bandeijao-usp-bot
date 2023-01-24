import telebot, re
from .config import settings
from datetime import datetime
from .messages.messages import Message
from .scrapping.cardapio import Crawler


TOKEN=settings.SECRET_KEY


class Bot:

	bot = telebot.TeleBot(TOKEN)	

	@bot.message_handler(commands=['Quimicas', "Fisica", "Central", "Prefeitura"])
	def get_currently_meal(message):
		print(f'[{message.from_user.username} | {message.from_user.first_name} | GET:{message.text}- {datetime.now()}]')
		try:
			cardapio = Crawler(message.text)
			dados = cardapio.trata_dados('almoco')
			response = Message().cardapio(message.text, dados)
			bot.reply_to(message, response)
		except Exception as e:
			response = Message().error(message.text, e)
			bot.reply_to(message, response)

	@bot.message_handler(func=lambda T: True)
	def generic_handler(user_message):
		message = Message(user_message)
		if message.is_valid():
			print(f'[{user_message.from_user.username} | {user_message.from_user.first_name} - {datetime.now()}]')
			bot.reply_to(user_message, message.menu())
		else:
			bot.reply_to(user_message, "Mensagem inválida, tente novamente!")

		
bot = Bot().bot






