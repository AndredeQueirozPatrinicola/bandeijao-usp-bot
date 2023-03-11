import telebot, re
from .config import settings
from datetime import datetime
from .messages.messages import Message
from .scrapping.crawler import Crawler


TOKEN=settings.SECRET_KEY


class Bot:

	bot = telebot.TeleBot(TOKEN)	

	@bot.message_handler(commands=['Quimicas', "Fisica", "Central", "Prefeitura"])
	def get_currently_meal(self, message):
		try:
			crawler = Crawler(message.text)
			dados = [crawler.trata_dados('almoco'), crawler.trata_dados('jantar')]
			response = Message().cardapio(message.text, dados)
			print(f'[{message.from_user.username} | {message.from_user.first_name} | GET:{message.text} / Status: Ok! - {datetime.now()}]')
			self.bot.reply_to(message, response)
		except Exception as e:
			response = Message().error(message.text)
			print(f'[{message.from_user.username} | {message.from_user.first_name} | GET:{message.text} / Status: ERROR! {e} - {datetime.now()}]')
			self.bot.reply_to(message, response)

	@bot.message_handler(func=lambda T: True)
	def generic_handler(self, user_message):
		message = Message(user_message)
		if message.is_valid():
			print(f'[{user_message.from_user.username} | {user_message.from_user.first_name} - {datetime.now()}]')
			self.bot.reply_to(user_message, message.menu())
		else:
			self.bot.reply_to(user_message, "Mensagem inválida, tente novamente!")

		







