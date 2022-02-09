
from turtle import update
from dotenv import load_dotenv
import os
from telegram.ext import Updater, CommandHandler
import logging
import handlers


def main():
    load_dotenv()
    token  = os.environ.get("TOKEN")
    if token is None:
        print("token is None. Make sure You set it in .env file")
        return
    print("Hello World! {}".format(token))

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start = CommandHandler('start', handlers.start)
    dispatcher.add_handler(start)

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()