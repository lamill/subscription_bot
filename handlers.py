from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    context.bot.send_message(chat_id=update._effective_chat.id, text = "hello {} . Your id is {}".format(user.name, user.id))