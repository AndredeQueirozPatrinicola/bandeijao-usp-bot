from src.Bot.bot import bot
from time import sleep

def main():
    try:
        bot.infinity_polling(timeout=100, long_polling_timeout = 500)
    except:
        sleep(15)
        main()
    finally:
        print("Error")
        sleep(60)
        main()


if __name__ == '__main__':
    main()