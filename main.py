#!/usr/bin/python3

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import vault
from io import BytesIO

bot = Bot(token=vault.bot_token)

def newperson(update: Update, context: CallbackContext) -> None:
    url = 'https://thispersondoesnotexist.com/image'
    photo_req = requests.get(url)
    target_photo = BytesIO(photo_req.content)
    chat_id = update.message.chat_id
    bot.sendPhoto(chat_id, target_photo)

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    update.message.reply_text('Welcome to This Person Does Not Exist Bot. Please type /newperson to get new image.')

def main():
    updater = Updater(bot.token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('newperson', newperson))
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
