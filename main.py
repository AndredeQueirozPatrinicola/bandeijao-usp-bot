from src.Bot.bot import bot


if __name__ == '__main__':
    bot.infinity_polling(timeout=100, long_polling_timeout = 500)